import re
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any

from src.parser.utils import combine_lines, extract_lines_from_pdf

ITEM_REGEX = r"(\d+)(.*?)(\d+,\d{2})?(?:\s+(\d+,\d{2}))$"
item_regex = re.compile(ITEM_REGEX)

WEIGHTED_ITEM_REGEX = r"(.*)\s(\d,\d{3})\skg\s(\d,\d{2})\s€/kg$"
weighted_item_regex = re.compile(WEIGHTED_ITEM_REGEX)

# Very dumb, not validating if the date is actually correct
DATETIME_REGEX = r"^([0-3]\d)\/([0-1]\d)\/(20\d\d)\s([0-2]\d):([0-5]\d).*$"
datetime_regex = re.compile(DATETIME_REGEX)


@dataclass
class MercadonaReceipt:
    datetime: datetime
    items: list[dict[str, Any]]  # change to Item dataclass


class ReceiptCrawler:
    @classmethod
    def __return_groups_or_none(cls, line: str):
        match = item_regex.match(line)
        if match:
            groups = match.groups()

            return groups if not groups[1].startswith("%") else False
        else:
            return False

    @classmethod
    def __to_decimal(cls, number_str: str) -> Decimal:
        return Decimal(number_str.replace(",", "."))

    @classmethod
    def __groups_to_dict(cls, groups: tuple[str, ...]) -> dict[str, Any]:
        total = cls.__to_decimal(groups[3])

        item_name_match = weighted_item_regex.match(groups[1])
        if item_name_match:
            return {
                "amount": cls.__to_decimal(item_name_match.group(2)),
                "name": item_name_match.group(1),
                "cost_unit": cls.__to_decimal(item_name_match.group(3)),
                "cost_total": total,
            }
        else:
            amount = groups[0]
            name = groups[1]
            cost_unit = cls.__to_decimal(groups[2]) if groups[2] else total

            # Need to handle the case
            #   16 HUEVOS CAMPEROS
            # to turn into
            #   6 HUEVOS CAMPEROS
            units_len = len((total / cost_unit).to_eng_string()) if total > 0 else 1

            overflow = groups[0][units_len:]

            if overflow:
                amount = groups[0][:units_len]
                name = f"{overflow}{name}"

            return {
                "amount": int(amount),
                "name": name.strip(),
                "cost_unit": cost_unit,
                "cost_total": total,
            }

    @classmethod
    def extract_items(cls, path: str) -> MercadonaReceipt:
        lines = extract_lines_from_pdf(path)
        combined_lines = combine_lines(lines)

        pre_selected_lines: tuple[str, ...] = tuple(
            filter(None, map(cls.__return_groups_or_none, combined_lines))
        )

        for line in combined_lines:
            match = datetime_regex.match(line)
            if match:
                groups = match.groups()
                extracted_date = datetime(
                    int(groups[2]),
                    int(groups[1]),
                    int(groups[0]),
                    int(groups[3]),
                    int(groups[4]),
                )

        items = list(map(cls.__groups_to_dict, pre_selected_lines))  # type: ignore

        return MercadonaReceipt(datetime=extracted_date, items=items)

import re
from decimal import Decimal
from typing import Any

from src.parser.utils import combine_lines, extract_lines_from_pdf

ITEM_REGEX = r"(\d+)(.*?)(\d+,\d{2})?(?:\s+(\d+,\d{2}))$"
regex = re.compile(ITEM_REGEX)


class ReceiptCrawler:
    @classmethod
    def __return_groups_or_none(cls, line):
        match = regex.match(line)
        if match:
            groups = match.groups()

            return groups if not groups[1].startswith("%") else False
        else:
            return False

    @classmethod
    def __groups_to_dict(cls, groups):
        total = Decimal(groups[3].replace(",", "."))
        return {
            "amount": int(groups[0]),
            "name": groups[1].strip(),
            "cost_unit": Decimal(groups[2].replace(",", ".")) if groups[2] else total,
            "cost_total": total,
        }

    @classmethod
    def extract_items(cls, path: str) -> list[dict[str, Any]]:
        lines = extract_lines_from_pdf(path)
        combined_lines = combine_lines(lines)

        pre_selected_lines: list[str] = list(
            filter(None, map(cls.__return_groups_or_none, combined_lines))
        )

        return list(map(cls.__groups_to_dict, pre_selected_lines))

import re
from decimal import Decimal

from src.models.item import Item
from src.parser.base_parser import BaseReceiptParser

ITEM_REGEX = r"([\w\d][\w\d\s{1}]+?)\s{2,}(.*\s(-?\d+,\d{0,2}))"
item_regex = re.compile(ITEM_REGEX)

MULTIPLE_ITEM_REGEX = r"^\s*(\d+)\sx\s\(\s+(\d+,\d{0,2})\s+\)"
multiple_item_regex = re.compile(MULTIPLE_ITEM_REGEX)


class CarrefourReceiptParser(BaseReceiptParser):
    DATETIME_REGEX = r"([0-3]\d)\/([0-1]\d)\/(20\d\d)\s([0-2]\d):([0-5]\d):([0-5]\d)"
    DATETIME_FORMAT = "%d/%m/%Y %H:%M:%S"
    STORE_NAME = "carrefour"

    def _reduce_lines(self, lines: list[str] | None = None) -> list[str]:
        if lines is None:
            lines = self.lines
        hard_stop = lines.index("╔════════════════════════════════════════╗")
        return lines[:hard_stop]

    def _get_items_from_lines(self, lines: list[str]) -> list[Item]:
        items = []

        for match in item_regex.findall("\n".join(lines)):
            name = match[0]
            if name == "SUBTOTAL":
                continue

            cost_total = Decimal(match[2].replace(",", "."))
            submatches = multiple_item_regex.match(match[1])

            if submatches:
                amount = Decimal(submatches.group(1))
                cost_unit = Decimal(submatches.group(2).replace(",", "."))
            else:
                amount = Decimal(1)
                cost_unit = cost_total

            items.append(
                Item(
                    name=name, amount=amount, cost_total=cost_total, cost_unit=cost_unit
                )
            )

        return items

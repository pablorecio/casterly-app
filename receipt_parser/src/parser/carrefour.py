import re
from datetime import datetime
from decimal import Decimal

from src.models.item import Item
from src.models.receipt import Receipt
from src.parser.utils import extract_lines_from_pdf

ITEM_REGEX = r"([\w\d][\w\d\s{1}]+?)\s{2,}(.*\s(-?\d+,\d{0,2}))"
item_regex = re.compile(ITEM_REGEX)

MULTIPLE_ITEM_REGEX = r"^\s*(\d+)\sx\s\(\s+(\d+,\d{0,2})\s+\)"
multiple_item_regex = re.compile(MULTIPLE_ITEM_REGEX)

DATETIME_REGEX = r"^\s*([0-3]\d)\/([0-1]\d)\/(20\d\d)\s([0-2]\d):([0-5]\d):([0-5]\d).*$"
datetime_regex = re.compile(DATETIME_REGEX)


class ReceiptCrawler:
    @classmethod
    def extract_items(cls, path: str) -> Receipt:
        lines = extract_lines_from_pdf(path)
        # Ignores anything below
        reduced_lines = lines[
            : lines.index("╔════════════════════════════════════════╗")
        ]
        items = []

        for match in item_regex.findall("\n".join(reduced_lines)):
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

        for line in lines:
            match = datetime_regex.match(line)
            if match:
                groups = match.groups()
                extracted_date = datetime(
                    int(groups[2]),
                    int(groups[1]),
                    int(groups[0]),
                    int(groups[3]),
                    int(groups[4]),
                    int(groups[5]),
                )
                break

        return Receipt(datetime=extracted_date, items=items)

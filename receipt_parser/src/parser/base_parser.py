import logging
import re
from datetime import datetime

from src.models.item import Item
from src.models.receipt import Receipt
from src.parser.utils import extract_text_from_pdf

logger = logging.getLogger()
logger.setLevel("INFO")


class BaseReceiptParser:
    DATETIME_REGEX: str
    DATETIME_FORMAT: str
    STORE_NAME: str

    def __init__(self, path: str) -> None:
        self.path = path
        self.text = extract_text_from_pdf(self.path)
        self.lines = self.text.split("\n")
        self.extracted_date = self.__extract_date()

    def __extract_date(self) -> datetime:
        match = re.search(self.DATETIME_REGEX, self.text)

        if not match:
            logger.warning("Could not find a datetime in the receipt %s", self.path)
            return datetime.now()

        return datetime.strptime(match.group().strip(), self.DATETIME_FORMAT)

    def _reduce_lines(self, lines: list[str] | None = None) -> list[str]:
        raise NotImplementedError("Method needs to be implemented in a child class")

    def _get_items_from_lines(self, lines: list[str]) -> list[Item]:
        raise NotImplementedError("Method needs to be implemented in a child class")

    def get_receipt_model(self) -> Receipt:
        reduced_lines = self._reduce_lines()
        items = self._get_items_from_lines(reduced_lines)
        return Receipt(items=items, datetime=self.extracted_date, store=self.STORE_NAME)

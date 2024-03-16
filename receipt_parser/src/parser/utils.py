from decimal import Decimal

from pypdf import PdfReader


def extract_text_from_pdf(path: str) -> str:
    """
    Given the path of a pdf file, return a string the parsed contents.
    """
    reader = PdfReader(path)
    page = reader.pages[0]
    return page.extract_text()


def extract_lines_from_pdf(path: str) -> list[str]:
    """
    Given the path of a pdf file, return a list of strings with the parsed contents.
    """
    return extract_text_from_pdf(path).split("\n")


def to_decimal(number_str: str, comma_separator: str = ",") -> Decimal:
    if comma_separator not in (None, "."):
        number_str = number_str.replace(comma_separator, ".")
    return Decimal(number_str)

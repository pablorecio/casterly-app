from pypdf import PdfReader


def extract_lines_from_pdf(path: str) -> list[str]:
    """
    Given the path of a pdf file, return a list of strings with the parsed contents.
    """
    reader = PdfReader(path)
    page = reader.pages[0]
    return page.extract_text().split("\n")

from pypdf import PdfReader


def extract_lines_from_pdf(path: str) -> list[str]:
    """
    Given the path of a pdf file, return a list of strings with the parsed contents.
    """
    reader = PdfReader(path)
    page = reader.pages[0]
    return page.extract_text().split("\n")


def combine_lines(lines: list[str]) -> list[str]:
    """
    Function to join items in a single line, for instance:

        1PLATANO
        0,838 kg 1,99 €/kg 1,67
        1KIWI VERDE
        0,644 kg 2,95 €/kg 1,90

    Should turn into

        1PLATANO 0,838 kg 1,99 €/kg 1,67
        1KIWI VERDE 0,644 kg 2,95 €/kg 1,90
    """

    new_lines: list[str] = []

    for line in lines:
        if "€/kg" in line:
            new_lines[-1] += f" {line}"
        else:
            new_lines.append(line)

    return new_lines

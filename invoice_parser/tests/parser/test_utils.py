import pytest

from src.parser.utils import combine_lines


@pytest.mark.parametrize(
    ("lines","expected"),
    [
        ([], []),
        (
            [
                "1PLATANO",
                "0,838 kg 1,99 €/kg 1,67",
                "1KIWI VERDE",
                "0,644 kg 2,95 €/kg 1,90",
            ],
            [
                "1PLATANO 0,838 kg 1,99 €/kg 1,67",
                "1KIWI VERDE 0,644 kg 2,95 €/kg 1,90",
            ]
        ),
        (
            [
                "1PATATAS GAJO 1,90",
                "1KIWI VERDE",
                "0,644 kg 2,95 €/kg 1,90",
            ],
            [
                "1PATATAS GAJO 1,90",
                "1KIWI VERDE 0,644 kg 2,95 €/kg 1,90",
            ]
        )
    ]
)
def test_combine_lines(lines, expected):
    result = combine_lines(lines)

    assert result == expected

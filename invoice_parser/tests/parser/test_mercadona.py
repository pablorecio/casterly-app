from decimal import Decimal
from typing import Any

import pytest
from src.parser.mercadona import ReceiptCrawler


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (
            "invoice_parser/tests/parser/data/mercadona_01.pdf",
            [
                {
                    "amount": 1,
                    "name": "PATATAS GAJO",
                    "cost_unit": Decimal("1.90"),
                    "cost_total": Decimal("1.90"),
                },
                {
                    "amount": 1,
                    "name": "+PROT NATILLA VAINI",
                    "cost_unit": Decimal("1.75"),
                    "cost_total": Decimal("1.75"),
                },
                {
                    "amount": 1,
                    "name": "GOLOSINAS MIX PICA",
                    "cost_unit": Decimal("1.65"),
                    "cost_total": Decimal("1.65"),
                },
                {
                    "amount": 1,
                    "name": "BOLSA PAPEL",
                    "cost_unit": Decimal("0.10"),
                    "cost_total": Decimal("0.10"),
                },
            ],
        )
    ],
)
def test_mercadona_extract(path: str, expected: list[dict[str, Any]]):
    assert ReceiptCrawler.extract_items(path) == expected

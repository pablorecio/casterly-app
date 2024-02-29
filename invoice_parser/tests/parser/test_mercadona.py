from datetime import datetime
from decimal import Decimal
from typing import Any

import pytest
from src.parser.mercadona import MercadonaReceipt, ReceiptCrawler


@pytest.mark.parametrize(
    ("path", "expected_datetime", "expected_items"),
    [
        (
            "invoice_parser/tests/parser/data/mercadona_01.pdf",
            datetime(2024, 2, 19, 19, 19),
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
        ),
        (
            "invoice_parser/tests/parser/data/mercadona_02.pdf",
            datetime(2024, 2, 5, 18, 28),
            [
                {
                    "amount": 1,
                    "name": "LAVAV. MAQ. LIQUIDO",
                    "cost_unit": Decimal("2.95"),
                    "cost_total": Decimal("2.95"),
                },
                {
                    "amount": 1,
                    "name": "+PROT NATILLA VAINI",
                    "cost_unit": Decimal("1.75"),
                    "cost_total": Decimal("1.75"),
                },
                {
                    "amount": 1,
                    "name": "PATATAS GAJO",
                    "cost_unit": Decimal("1.90"),
                    "cost_total": Decimal("1.90"),
                },
                {
                    "amount": 1,
                    "name": "TORTITA MAIZ C/CHOCO",
                    "cost_unit": Decimal("1.65"),
                    "cost_total": Decimal("1.65"),
                },
                {
                    "amount": 1,
                    "name": "TORTITAS DE MAIZ",
                    "cost_unit": Decimal("1.10"),
                    "cost_total": Decimal("1.10"),
                },
                {
                    "amount": 1,
                    "name": "BOLSA RAFIA",
                    "cost_unit": Decimal("0.65"),
                    "cost_total": Decimal("0.65"),
                },
                {
                    "amount": 1,
                    "name": "LECHE SEMI S/LACT",
                    "cost_unit": Decimal("5.70"),
                    "cost_total": Decimal("5.70"),
                },
                {
                    "amount": 2,
                    "name": "COPOS DE AVENA",
                    "cost_unit": Decimal("0.95"),
                    "cost_total": Decimal("1.90"),
                },
                {
                    "amount": 1,
                    "name": "REBUENAS",
                    "cost_unit": Decimal("1.20"),
                    "cost_total": Decimal("1.20"),
                },
                {
                    "amount": 1,
                    "name": "BASTONCILLO FAMIL",
                    "cost_unit": Decimal("0.90"),
                    "cost_total": Decimal("0.90"),
                },
                {
                    "amount": 1,
                    "name": "SAL YODADA",
                    "cost_unit": Decimal("0.35"),
                    "cost_total": Decimal("0.35"),
                },
                {
                    "amount": 1,
                    "name": "F+L CARIBE S AZÚCAR",
                    "cost_unit": Decimal("1.20"),
                    "cost_total": Decimal("1.20"),
                },
                {
                    "amount": 1,
                    "name": "ARROZ COCIDO",
                    "cost_unit": Decimal("1.15"),
                    "cost_total": Decimal("1.15"),
                },
                {
                    "amount": 1,
                    "name": "LOMO ADOBADO",
                    "cost_unit": Decimal("3.56"),
                    "cost_total": Decimal("3.56"),
                },
                {
                    "amount": 1,
                    "name": "FRESÓN",
                    "cost_unit": Decimal("3.26"),
                    "cost_total": Decimal("3.26"),
                },
                {
                    "amount": 1,
                    "name": "XUXES TOP TEN",
                    "cost_unit": Decimal("1.25"),
                    "cost_total": Decimal("1.25"),
                },
                {
                    "amount": 1,
                    "name": "SALMOREJO FRESCO",
                    "cost_unit": Decimal("1.30"),
                    "cost_total": Decimal("1.30"),
                },
                {
                    "amount": 1,
                    "name": "FRITADA PISTO",
                    "cost_unit": Decimal("1.30"),
                    "cost_total": Decimal("1.30"),
                },
                {
                    "amount": 1,
                    "name": "6 HUEVOS CAMPEROS",
                    "cost_unit": Decimal("1.59"),
                    "cost_total": Decimal("1.59"),
                },
                {
                    "amount": Decimal("0.838"),
                    "name": "PLATANO",
                    "cost_unit": Decimal("1.99"),
                    "cost_total": Decimal("1.67"),
                },
                {
                    "amount": Decimal("0.644"),
                    "name": "KIWI VERDE",
                    "cost_unit": Decimal("2.95"),
                    "cost_total": Decimal("1.90"),
                },
            ],
        ),
    ],
)
def test_mercadona_extract(
    path: str, expected_datetime: datetime, expected_items: list[dict[str, Any]]
):
    expected = MercadonaReceipt(datetime=expected_datetime, items=expected_items)
    assert ReceiptCrawler.extract_items(path) == expected

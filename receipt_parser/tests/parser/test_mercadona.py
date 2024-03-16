from datetime import datetime
from decimal import Decimal

import pytest
from src.models.item import Item
from src.models.receipt import Receipt
from src.parser.mercadona import MercadonaReceiptCrawler


@pytest.mark.parametrize(
    ("path", "expected_datetime", "expected_items", "total_amount"),
    [
        (
            "receipt_parser/tests/parser/data/mercadona_01.pdf",
            datetime(2024, 2, 19, 19, 19),
            [
                Item(
                    amount=Decimal(1),
                    name="PATATAS GAJO",
                    cost_unit=Decimal("1.90"),
                    cost_total=Decimal("1.90"),
                ),
                Item(
                    amount=Decimal(1),
                    name="+PROT NATILLA VAINI",
                    cost_unit=Decimal("1.75"),
                    cost_total=Decimal("1.75"),
                ),
                Item(
                    amount=Decimal(1),
                    name="GOLOSINAS MIX PICA",
                    cost_unit=Decimal("1.65"),
                    cost_total=Decimal("1.65"),
                ),
                Item(
                    amount=Decimal(1),
                    name="BOLSA PAPEL",
                    cost_unit=Decimal("0.10"),
                    cost_total=Decimal("0.10"),
                ),
            ],
            Decimal("5.40"),
        ),
        (
            "receipt_parser/tests/parser/data/mercadona_02.pdf",
            datetime(2024, 2, 5, 18, 28),
            [
                Item(
                    amount=Decimal(1),
                    name="LAVAV. MAQ. LIQUIDO",
                    cost_unit=Decimal("2.95"),
                    cost_total=Decimal("2.95"),
                ),
                Item(
                    amount=Decimal(1),
                    name="+PROT NATILLA VAINI",
                    cost_unit=Decimal("1.75"),
                    cost_total=Decimal("1.75"),
                ),
                Item(
                    amount=Decimal(1),
                    name="PATATAS GAJO",
                    cost_unit=Decimal("1.90"),
                    cost_total=Decimal("1.90"),
                ),
                Item(
                    amount=Decimal(1),
                    name="TORTITA MAIZ C/CHOCO",
                    cost_unit=Decimal("1.65"),
                    cost_total=Decimal("1.65"),
                ),
                Item(
                    amount=Decimal(1),
                    name="TORTITAS DE MAIZ",
                    cost_unit=Decimal("1.10"),
                    cost_total=Decimal("1.10"),
                ),
                Item(
                    amount=Decimal(1),
                    name="BOLSA RAFIA",
                    cost_unit=Decimal("0.65"),
                    cost_total=Decimal("0.65"),
                ),
                Item(
                    amount=Decimal(1),
                    name="LECHE SEMI S/LACT",
                    cost_unit=Decimal("5.70"),
                    cost_total=Decimal("5.70"),
                ),
                Item(
                    amount=Decimal(2),
                    name="COPOS DE AVENA",
                    cost_unit=Decimal("0.95"),
                    cost_total=Decimal("1.90"),
                ),
                Item(
                    amount=Decimal(1),
                    name="REBUENAS",
                    cost_unit=Decimal("1.20"),
                    cost_total=Decimal("1.20"),
                ),
                Item(
                    amount=Decimal(1),
                    name="BASTONCILLO FAMIL",
                    cost_unit=Decimal("0.90"),
                    cost_total=Decimal("0.90"),
                ),
                Item(
                    amount=Decimal(1),
                    name="SAL YODADA",
                    cost_unit=Decimal("0.35"),
                    cost_total=Decimal("0.35"),
                ),
                Item(
                    amount=Decimal(1),
                    name="F+L CARIBE S AZÚCAR",
                    cost_unit=Decimal("1.20"),
                    cost_total=Decimal("1.20"),
                ),
                Item(
                    amount=Decimal(1),
                    name="ARROZ COCIDO",
                    cost_unit=Decimal("1.15"),
                    cost_total=Decimal("1.15"),
                ),
                Item(
                    amount=Decimal(1),
                    name="LOMO ADOBADO",
                    cost_unit=Decimal("3.56"),
                    cost_total=Decimal("3.56"),
                ),
                Item(
                    amount=Decimal(1),
                    name="FRESÓN",
                    cost_unit=Decimal("3.26"),
                    cost_total=Decimal("3.26"),
                ),
                Item(
                    amount=Decimal(1),
                    name="XUXES TOP TEN",
                    cost_unit=Decimal("1.25"),
                    cost_total=Decimal("1.25"),
                ),
                Item(
                    amount=Decimal(1),
                    name="SALMOREJO FRESCO",
                    cost_unit=Decimal("1.30"),
                    cost_total=Decimal("1.30"),
                ),
                Item(
                    amount=Decimal(1),
                    name="FRITADA PISTO",
                    cost_unit=Decimal("1.30"),
                    cost_total=Decimal("1.30"),
                ),
                Item(
                    amount=Decimal(1),
                    name="6 HUEVOS CAMPEROS",
                    cost_unit=Decimal("1.59"),
                    cost_total=Decimal("1.59"),
                ),
                Item(
                    amount=Decimal("0.838"),
                    name="PLATANO",
                    cost_unit=Decimal("1.99"),
                    cost_total=Decimal("1.67"),
                ),
                Item(
                    amount=Decimal("0.644"),
                    name="KIWI VERDE",
                    cost_unit=Decimal("2.95"),
                    cost_total=Decimal("1.90"),
                ),
            ],
            Decimal("38.23"),
        ),
    ],
)
def test_mercadona_extract(
    path: str,
    expected_datetime: datetime,
    expected_items: list[Item],
    total_amount: Decimal,
):
    crawler = MercadonaReceiptCrawler(path)
    result = crawler.get_receipt_model()
    expected = Receipt(
        datetime=expected_datetime, items=expected_items, store="mercadona"
    )
    assert result == expected
    assert result.total_amount == total_amount

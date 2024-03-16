from datetime import datetime
from decimal import Decimal

import pytest
from src.models.item import Item
from src.models.receipt import Receipt
from src.parser.carrefour import ReceiptCrawler


@pytest.mark.parametrize(
    ("path", "expected_datetime", "expected_items", "total_amount"),
    [
        (
            "receipt_parser/tests/parser/data/carrefour_01.pdf",
            datetime(2024, 3, 14, 15, 22, 13),
            [
                Item(
                    name="CROFT TWIST BCO 75",
                    amount=Decimal(1),
                    cost_unit=Decimal("8.49"),
                    cost_total=Decimal("8.49"),
                ),
                Item(
                    name="VINO ARABE",
                    amount=Decimal(1),
                    cost_unit=Decimal("3.85"),
                    cost_total=Decimal("3.85"),
                ),
                Item(
                    name="CARAMELOS SELECTION",
                    amount=Decimal(1),
                    cost_unit=Decimal("1.67"),
                    cost_total=Decimal("1.67"),
                ),
                Item(
                    name="FAVORITOS AZUCAR 90G",
                    amount=Decimal(1),
                    cost_unit=Decimal("1.29"),
                    cost_total=Decimal("1.29"),
                ),
                Item(
                    name="PANECILLOS NAANS",
                    amount=Decimal(1),
                    cost_unit=Decimal("4.19"),
                    cost_total=Decimal("4.19"),
                ),
                Item(
                    name="PANKO JAPON",
                    amount=Decimal(1),
                    cost_unit=Decimal("3.39"),
                    cost_total=Decimal("3.39"),
                ),
                Item(
                    name="REGALIZ RED MIX FINI",
                    amount=Decimal(1),
                    cost_unit=Decimal("1.74"),
                    cost_total=Decimal("1.74"),
                ),
                Item(
                    name="BEBIDA DE AVENA",
                    amount=Decimal(6),
                    cost_unit=Decimal("0.95"),
                    cost_total=Decimal("5.70"),
                ),
                Item(
                    name="BOLSA 48X60CM",
                    amount=Decimal(1),
                    cost_unit=Decimal("0.15"),
                    cost_total=Decimal("0.15"),
                ),
                Item(
                    name="CUPON",
                    amount=Decimal(1),
                    cost_unit=Decimal("-1.43"),
                    cost_total=Decimal("-1.43"),
                ),
                Item(
                    name="CHEQUE AHORRO",
                    amount=Decimal(1),
                    cost_unit=Decimal("-21.68"),
                    cost_total=Decimal("-21.68"),
                ),
                Item(
                    name="QUE VUELVE 1",
                    amount=Decimal(1),
                    cost_unit=Decimal("-0.38"),
                    cost_total=Decimal("-0.38"),
                ),
                Item(
                    name="QUE VUELVE 1",
                    amount=Decimal(1),
                    cost_unit=Decimal("-1.68"),
                    cost_total=Decimal("-1.68"),
                ),
            ],
            Decimal("5.30"),
        ),
        (
            "receipt_parser/tests/parser/data/carrefour_02.pdf",
            datetime(2024, 2, 12, 11, 49, 33),
            [
                Item(
                    name="ACEITE OLIVA MASIA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("7.89"),
                    cost_total=Decimal("7.89"),
                ),
                Item(
                    name="GINGER FEVERTREE",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.59"),
                    cost_total=Decimal("1.59"),
                ),
                Item(
                    name="SCHWEPPES PREMIUM",
                    amount=Decimal("2"),
                    cost_unit=Decimal("1.75"),
                    cost_total=Decimal("3.50"),
                ),
                Item(
                    name="VINO EL GRAN JEFE",
                    amount=Decimal("1"),
                    cost_unit=Decimal("5.99"),
                    cost_total=Decimal("5.99"),
                ),
                Item(
                    name="DESODORANTE 200 ML",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.80"),
                    cost_total=Decimal("1.80"),
                ),
                Item(
                    name="PAPEL COCINA X4           CP00",
                    amount=Decimal("2"),
                    cost_unit=Decimal("2.59"),
                    cost_total=Decimal("5.18"),
                ),
                Item(
                    name="DESCUENTO EN 2ª UNIDAD",
                    amount=Decimal("1"),
                    cost_unit=Decimal("-1.30"),
                    cost_total=Decimal("-1.30"),
                ),
                Item(
                    name="CEPILLO GREEN MEDIO",
                    amount=Decimal("2"),
                    cost_unit=Decimal("4.95"),
                    cost_total=Decimal("9.90"),
                ),
                Item(
                    name="ACEITUNAS CARREFOUR",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.99"),
                    cost_total=Decimal("1.99"),
                ),
                Item(
                    name="AVENA CARREFOUR",
                    amount=Decimal("1"),
                    cost_unit=Decimal("0.85"),
                    cost_total=Decimal("0.85"),
                ),
                Item(
                    name="CAFÉ CREMA 1KG",
                    amount=Decimal("1"),
                    cost_unit=Decimal("15.49"),
                    cost_total=Decimal("15.49"),
                ),
                Item(
                    name="CALDO VERDURAS 1L",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.05"),
                    cost_total=Decimal("1.05"),
                ),
                Item(
                    name="FILETE ANCHOA ACEITE",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.35"),
                    cost_total=Decimal("2.35"),
                ),
                Item(
                    name="GALLETA DIGESTIVE",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.25"),
                    cost_total=Decimal("2.25"),
                ),
                Item(
                    name="SOPA KNORR LETRAS",
                    amount=Decimal("1"),
                    cost_unit=Decimal("0.76"),
                    cost_total=Decimal("0.76"),
                ),
                Item(
                    name="SOPA TERNERA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.49"),
                    cost_total=Decimal("2.49"),
                ),
                Item(
                    name="PIZZA POLLO",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.65"),
                    cost_total=Decimal("2.65"),
                ),
                Item(
                    name="CHORIZO JABUGUITO",
                    amount=Decimal("1"),
                    cost_unit=Decimal("6.19"),
                    cost_total=Decimal("6.19"),
                ),
                Item(
                    name="MERLUZA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("3.34"),
                    cost_total=Decimal("3.34"),
                ),
                Item(
                    name="ARANDANOS 225",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.69"),
                    cost_total=Decimal("2.69"),
                ),
                Item(
                    name="BANANA GRANEL",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.55"),
                    cost_total=Decimal("1.55"),
                ),
                Item(
                    name="BROCOLI FLORETES",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.99"),
                    cost_total=Decimal("1.99"),
                ),
                Item(
                    name="BROTES DELUXE",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.79"),
                    cost_total=Decimal("1.79"),
                ),
                Item(
                    name="CALABAZA SEPALLO",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.54"),
                    cost_total=Decimal("2.54"),
                ),
                Item(
                    name="CEBOLLA ROJA 500G",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.45"),
                    cost_total=Decimal("1.45"),
                ),
                Item(
                    name="CIRUELA ROJA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.09"),
                    cost_total=Decimal("1.09"),
                ),
                Item(
                    name="FRESAS 400G",
                    amount=Decimal("1"),
                    cost_unit=Decimal("3.29"),
                    cost_total=Decimal("3.29"),
                ),
                Item(
                    name="JENGIBRE",
                    amount=Decimal("1"),
                    cost_unit=Decimal("0.24"),
                    cost_total=Decimal("0.24"),
                ),
                Item(
                    name="KIWI BIO 500 GRAMOS",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.99"),
                    cost_total=Decimal("2.99"),
                ),
                Item(
                    name="MANDARINA CDC 1KG",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.65"),
                    cost_total=Decimal("2.65"),
                ),
                Item(
                    name="PATATA GRANEL",
                    amount=Decimal("1"),
                    cost_unit=Decimal("0.80"),
                    cost_total=Decimal("0.80"),
                ),
                Item(
                    name="PLATANO",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.59"),
                    cost_total=Decimal("2.59"),
                ),
                Item(
                    name="SETA SHI TAKE",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.96"),
                    cost_total=Decimal("2.96"),
                ),
                Item(
                    name="TOMATE CHERRY MINI",
                    amount=Decimal("1"),
                    cost_unit=Decimal("1.49"),
                    cost_total=Decimal("1.49"),
                ),
                Item(
                    name="UVA BICOLOR CRF 500",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.75"),
                    cost_total=Decimal("2.75"),
                ),
                Item(
                    name="ZANAHORIA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.15"),
                    cost_total=Decimal("2.15"),
                ),
                Item(
                    name="CHULETA PAVO AJILLO",
                    amount=Decimal("1"),
                    cost_unit=Decimal("4.49"),
                    cost_total=Decimal("4.49"),
                ),
                Item(
                    name="L DECENA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("3.79"),
                    cost_total=Decimal("3.79"),
                ),
                Item(
                    name="PECHUGA MARINADA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("3.77"),
                    cost_total=Decimal("3.77"),
                ),
                Item(
                    name="PIMIENTO ASADO TIRA",
                    amount=Decimal("1"),
                    cost_unit=Decimal("2.99"),
                    cost_total=Decimal("2.99"),
                ),
                Item(
                    name="2FIBRA VERDE",
                    amount=Decimal("2"),
                    cost_unit=Decimal("1.69"),
                    cost_total=Decimal("3.38"),
                ),
            ],
            Decimal("127.39"),
        ),
    ],
)
def test_carrefour_extract(
    path: str,
    expected_datetime: datetime,
    expected_items: list[Item],
    total_amount: Decimal,
):
    result = ReceiptCrawler.extract_items(path)
    expected = Receipt(
        datetime=expected_datetime, items=expected_items, store="carrefour"
    )
    assert result == expected
    assert result.total_amount == total_amount

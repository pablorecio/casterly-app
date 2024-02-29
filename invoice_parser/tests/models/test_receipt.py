from datetime import datetime
from decimal import Decimal

import pytest
from src.models.item import Item
from src.models.receipt import Receipt


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        ([], Decimal(0)),
        (
            [
                Item(
                    name="LECHE",
                    amount=Decimal(1),
                    cost_unit=Decimal("1.56"),
                    cost_total=Decimal("1.56"),
                ),
            ],
            Decimal("1.56"),
        ),
        (
            [
                Item(
                    name="LECHE",
                    amount=Decimal(1),
                    cost_unit=Decimal("1.56"),
                    cost_total=Decimal("1.56"),
                ),
                Item(
                    name="TORTITAS MAIZ",
                    amount=Decimal(2),
                    cost_unit=Decimal("1.99"),
                    cost_total=Decimal("3.98"),
                ),
            ],
            Decimal("5.54"),
        ),
    ],
)
def test_total_amount(items: list[Item], expected: Decimal):
    receipt = Receipt(datetime=datetime.now(), items=items)
    assert receipt.total_amount == expected

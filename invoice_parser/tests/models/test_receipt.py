import json
from datetime import datetime
from decimal import Decimal
from typing import Any

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


@pytest.mark.parametrize(
    ("items", "dt", "expected"),
    [
        (
            [],
            datetime(2023, 12, 21),
            {
                "datetime": datetime(2023, 12, 21).strftime("%Y-%m-%dT%H:%M:%S"),
                "items": [],
                "total_amount": "0",
            },
        ),
        (
            [
                Item(
                    name="LECHE",
                    amount=Decimal(1),
                    cost_unit=Decimal("1.56"),
                    cost_total=Decimal("1.56"),
                ),
            ],
            datetime(2023, 12, 21),
            {
                "datetime": datetime(2023, 12, 21).strftime("%Y-%m-%dT%H:%M:%S"),
                "items": [
                    {
                        "name": "LECHE",
                        "amount": "1",
                        "cost_unit": "1.56",
                        "cost_total": "1.56",
                    }
                ],
                "total_amount": "1.56",
            },
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
            datetime(2023, 12, 21),
            {
                "datetime": datetime(2023, 12, 21).strftime("%Y-%m-%dT%H:%M:%S"),
                "items": [
                    {
                        "name": "LECHE",
                        "amount": "1",
                        "cost_unit": "1.56",
                        "cost_total": "1.56",
                    },
                    {
                        "name": "TORTITAS MAIZ",
                        "amount": "2",
                        "cost_unit": "1.99",
                        "cost_total": "3.98",
                    },
                ],
                "total_amount": "5.54",
            },
        ),
    ],
)
def test_model_serializer(items: list[Item], dt: datetime, expected: dict[str, Any]):
    receipt = Receipt(datetime=dt, items=items)
    assert json.loads(receipt.model_dump_json()) == expected

from decimal import Decimal

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    amount: Decimal
    cost_unit: Decimal
    cost_total: Decimal

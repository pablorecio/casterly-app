from datetime import datetime

from pydantic import BaseModel
from src.models.item import Item


class Receipt(BaseModel):
    datetime: datetime
    items: list[Item]

    @property
    def total_amount(self):
        return sum([i.cost_total for i in self.items])

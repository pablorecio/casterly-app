from datetime import datetime
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, model_serializer
from src.models.item import Item


class Receipt(BaseModel):
    datetime: datetime
    items: list[Item]

    @property
    def total_amount(self) -> Decimal:
        return Decimal(sum([i.cost_total for i in self.items]))

    def output_to_file(self, path: str) -> None:
        output = self.model_dump_json()
        f = open(path, "w")
        f.write(output)

    @model_serializer()
    def serialize_model(self) -> dict[str, Any]:
        return {
            "datetime": self.datetime,
            "items": self.items,
            "total_amount": self.total_amount,
        }

from __future__ import annotations

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name

    @property
    def get_price(self) -> str:
        return f'{self.price // 100} $'

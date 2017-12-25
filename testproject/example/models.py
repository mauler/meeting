from django.db import models

from meeting.common.managers import BaseManager
from meeting.common.models import BaseModel


class Purchase(BaseModel):
    def __str__(self):
        return self.created_on.strftime('%Y-%m-%d')


class PurchaseItem(BaseModel):
    objects = BaseManager(this_year_lookup='purchase__created_on__year')

    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)

    def __str__(self):
        return self.created_on.strftime('%Y-%m-%d')

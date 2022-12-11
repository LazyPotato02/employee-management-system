from django.db import models
from django.core import validators

from employee_management_sys.cells.models import Cells

# Create your models here.
'''
https://docs.djangoproject.com/en/4.1/topics/db/examples/one_to_one/
'''

class Order(models.Model):
    name = models.CharField(
        max_length=255,
    )
    quantity = models.PositiveIntegerField()
    cell = models.OneToOneField(
        Cells,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    is_done = models.BooleanField()

    def __str__(self):
        return self.name
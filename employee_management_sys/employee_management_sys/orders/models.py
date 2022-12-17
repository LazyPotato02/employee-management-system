from django.db import models
from django.core import validators

from employee_management_sys.cells.models import Cells

# Create your models here.

class Order(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(
        max_length=255,
        unique=True,
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
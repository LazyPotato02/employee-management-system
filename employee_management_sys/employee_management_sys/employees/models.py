from django.core import validators
from django.db import models

# Create your models here.
from employee_management_sys.base.validators import validate_only_letters
from employee_management_sys.cells.models import Cells


class Employee(models.Model):
    class Meta:
        ordering = ('first_name',)

    C01 = "C01"
    C02 = "C02"
    C03 = "C03"
    C04 = "C04"
    C05 = "C05"
    CELLS = (
        (C01, C01),
        (C02, C02),
        (C03, C03),
        (C04, C04),
        (C05, C05),
    )
    first_name = models.CharField(
        max_length=40,
        validators=(
            validate_only_letters,
            validators.MinLengthValidator(2),
        ),
        verbose_name='First Name',
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=40,
        validators=(
            validate_only_letters,
            validators.MinLengthValidator(2),
        ),
        verbose_name='Last Name',
        blank=False,
        null=False,
    )

    cell = models.ManyToManyField(Cells)
    emp_id = models.CharField(
        max_length=7,
        unique=True,
        verbose_name='Employee Id'
    )

    def __repr__(self):
        return str(self.cell.get())

    def __str__(self):
        return f"{self.cell.get()}"

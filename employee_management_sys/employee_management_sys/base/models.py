from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.
from employee_management_sys.base.validators import validate_only_letters
from employee_management_sys.cells.models import Cells
from employee_management_sys.employees.models import Employee


class EmployeeManager(auth_models.AbstractUser):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True

    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
            validate_only_letters,
        ),
        null=True,
        blank=True
    )

    email = models.EmailField(
        unique=True,
        null=True,
    )

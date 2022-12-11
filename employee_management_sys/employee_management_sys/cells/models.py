from django.db import models

# Create your models here.


class Cells(models.Model):
    class Meta:
        ordering = ['cell_name']

    cell_name = models.CharField(max_length=25,unique=True)

    def __repr__(self):
        return self.cell_name

    def __str__(self):
        return self.cell_name

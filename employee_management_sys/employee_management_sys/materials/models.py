from django.db import models

# Create your models here.

class Materials(models.Model):
    class Meta:
        ordering = ['name']
    name = models.CharField(
        max_length=255,
    )
    quantity = models.PositiveIntegerField()
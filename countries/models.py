from django.db import models


class Country(models.Model):
    name = models.CharField('Name of countries', max_length=200, unique=True, null=False)

    def __str__(self):
        return f'Country:{self.name}'

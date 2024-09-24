from django.db import models
from django.utils import timezone


class CreateUpdateMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class University(CreateUpdateMixin):
    name = models.CharField(max_length=200, unique=True, null=False)
    rank = models.IntegerField(unique=True, null=False)
    score = models.FloatField(null=False)
    country = models.ForeignKey('countries.Country', on_delete=models.CASCADE)

    def __str__(self):
        return f'University: {self.name}'

    # class Meta:
    #     db_table = 'universities'


class Student(CreateUpdateMixin):
    name = models.CharField(max_length=100, null=False)
    university = models.ManyToManyField(University)

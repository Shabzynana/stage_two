from django.db import models

class Person(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return self.name

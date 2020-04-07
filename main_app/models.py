from django.db import models

# Create your models here.


class Scent(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    characteristics = models.TextField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

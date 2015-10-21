from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    eye_color = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Shoe(models.Model):
    owner = models.ForeignKey(Person)
    size = models.IntegerField()

    def __str__(self):
        return str(self.size)
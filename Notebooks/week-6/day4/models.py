from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    eye_color = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Shoe(models.Model):
    owner = models.ForeignKey(Person)
    color = models.CharField(max_length=20, blank=True)
    make = models.CharField(max_length=100, blank=True)
    size = models.IntegerField()

    def __str__(self):
        return str(self.size)


class Genre(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
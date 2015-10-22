from django.contrib import admin

from helloworld.models import Shoe, Person, Movie, Genre

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Genre)

# ./manage.py createsuperuser
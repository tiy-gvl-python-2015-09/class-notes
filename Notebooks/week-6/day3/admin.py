from django.contrib import admin

from helloworld.models import Shoe, Person

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Person)

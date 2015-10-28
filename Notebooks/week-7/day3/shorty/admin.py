from django.contrib import admin

# Register your models here.
from shorty.models import UrlRecord, UrlCounter

admin.site.register(UrlRecord)
admin.site.register(UrlCounter)

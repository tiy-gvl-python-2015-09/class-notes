from django.contrib import admin

# Register your models here.
from pandas_data.models import StudentRecord

admin.site.register(StudentRecord)

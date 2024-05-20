from django.contrib import admin
from django.contrib.auth.models import User
from kol.models import Phone,Manufacturer

admin.site.register(Phone)
admin.site.register(Manufacturer)

# Register your models here.

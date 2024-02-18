from django.contrib import admin

# Register your models here.
from .models import Client, Package, Transportist

admin.site.register([Client, Package, Transportist])

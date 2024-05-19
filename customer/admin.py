from django.contrib import admin
from .models import Customer
from django.contrib.auth.models import Group, User as AuthUser

# Register your models here.
admin.site.register(Customer)

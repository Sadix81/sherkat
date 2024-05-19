from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User  , on_delete=models.CASCADE , null=True , blank=True)
    


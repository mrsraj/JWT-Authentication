# from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser 
from django.db import models

class CustomUser (AbstractUser):
    # Add any additional fields you want
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
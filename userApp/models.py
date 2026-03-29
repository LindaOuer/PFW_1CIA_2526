from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    user_id = models.CharField(primary_key=True, unique=True, editable=False, max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        ('participant', 'Participant'), 
        ('committee', 'Committee'), 
        ('member', 'Member')], 
    default='participant')
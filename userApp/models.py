from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError


def validateEmail(value):
    domains = ['esprit.tn', 'univ.tn']
    domain = value.split('@')[-1]
    if domain not in domains:
        raise ValidationError(f"Email domain '{domain}' is not allowed")

name_validator = RegexValidator(
    regex=r'^[a-zA-Z]+$',
    message='Name must contain only letters'
)

class User(AbstractUser):
    user_id = models.CharField(primary_key=True, unique=True, editable=False, max_length=100)
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(3, 'Name must have more characters'), name_validator])
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(5, 'Name must have more characters'), name_validator])
    email = models.EmailField(unique=True, validators=[validateEmail])
    affiliation = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        ('participant', 'Participant'), 
        ('committee', 'Committee'), 
        ('member', 'Member')], 
    default='participant')
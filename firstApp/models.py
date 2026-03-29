from django.db import models

# Create your models here.

class Classe(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=2025)


class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    dob= models.DateField()
    address = models.TextField(default="Tunis")
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, blank=True)
    # or you can use models.SET_NULL if you want to keep the student even if the class is deleted
    # or you can use models.PROTECT if you want to prevent deletion of the class if there are students associated with it

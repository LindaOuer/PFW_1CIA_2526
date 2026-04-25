from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Session (models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=10, validators=[
        RegexValidator(regex=r'^[a-zA-Z0-9]+$', 
                       message='Name must contain only letters and can include spaces')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__ (self):
        return self.title

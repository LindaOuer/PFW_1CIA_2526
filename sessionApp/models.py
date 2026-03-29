from django.db import models

# Create your models here.

class Session (models.Model):
    session_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__ (self):
        return self.title
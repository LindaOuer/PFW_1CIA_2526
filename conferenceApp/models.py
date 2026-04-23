from django.db import models

from userApp.models import User
from django.core.validators  import MinLengthValidator, MaxLengthValidator, FileExtensionValidator

# Create your models here.


class Conference(models.Model):
    THEME_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('SE', 'Software Engineering'),
        ('SSE', 'Social Sciences & Education'),
        ('INT', 'Interdisciplinenary Themes'),
    ]

    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(validators=[
        MinLengthValidator(30, 'Description must be at least 30 characters long'),
        MaxLengthValidator(300, 'Description must have at most 300 characters')
    ])
    theme = models.CharField(max_length=100, choices = THEME_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    userSubmissions = models.ManyToManyField(User, through="Submission", related_name='submitted_conferences')
    organizingCommittees = models.ManyToManyField(User, through="OrganizingCommittee", related_name='organized_conferences')
    

class OrganizingCommittee(models.Model):
    ROLE_CHOICES = [
        ('Chair', 'Chair'),
        ('Co-Chair', 'Co-Chair'),
        ('Member', 'Member'),
    ]
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='committees')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    committee_role = models.CharField(max_length=100, choices=ROLE_CHOICES)
    date_joined = models.DateField(auto_now_add=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Submission(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Under Review', 'Under Review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    paper = models.FileField(upload_to='papers/', validators=[
        FileExtensionValidator(allowed_extensions=["pdf"])
    ])
    
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Submitted')
    payed = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models

from userApp.models import User
from django.core.validators  import MinLengthValidator, MaxLengthValidator, FileExtensionValidator, RegexValidator
from django.utils.timezone import now
from django.core.exceptions import ValidationError

# Create your models here.


class Conference(models.Model):
    THEME_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('SE', 'Software Engineering'),
        ('SSE', 'Social Sciences & Education'),
        ('INT', 'Interdisciplinenary Themes'),
    ]

    conference_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, validators=[
        RegexValidator(regex=r'^[a-zA-Z\s]+$', 
                       message='Name must contain only letters and can include spaces')
    ])
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
    
    def clean(self):
        if self.start_date is None or self.end_date is None:
            raise ValidationError("Start date and end date cannot be null.")
        
        if now().date() > self.start_date:
            raise ValidationError("Start date cannot be in the past.")

        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")
    

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
    
   

def validate_keywords(value):
    list = [k.strip() for k in value.split(",") if k.strip()]
    if len(list) > 10:
        raise ValidationError("A maximum of 10 keywords is allowed.")
 
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
    keywords = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        if self.conference:
            if self.conference.start_date < now().date():
                raise ValidationError("Cannot submit to a conference that has already started.")
        if self.user and self.submission_date:
            countSubmissions = Submission.objects.filter(user=self.user, submission_date=self.submission_date).count()
            if countSubmissions > 3:
                raise ValidationError("A user can submit a maximum of 3 papers per conference.")
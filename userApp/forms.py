from django.contrib.auth.forms import UserCreationForm
from .models import User 

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        # Include your specific attributes here
        fields = (
            'username',
            'first_name', 
            'last_name', 
            'email', 
            'affiliation', 
            'nationality', 
            'role',
            'password1',
            'password2',
        )
from django.shortcuts import render
from .models import Conference

# Create your views here.
def conference_list(request):
    list = Conference.objects.all()
    # SELECT * FROM conference
    return render(request, 'conferences/conference_list.html', {'conferences': list})

def home(request):
    return render(request, 'conferences/home.html')

def name(request, n):
    students = {
        'st1': {"name" : 'Alice'},
        'st2': {"name" : 'Bob'},
    }
    return render(request, 
                  'conferences/name.html', 
                  {'name': '1CIA', 'pathVar': n, 'students': students})
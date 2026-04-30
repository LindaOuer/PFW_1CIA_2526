from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Conference

# Create your views here.
def conference_list(request):
    list = Conference.objects.all().order_by('-start_date')
    # SELECT * FROM conference ORDER BY start_date DESC
    return render(request, 'conferences/conference_list.html', {'conferences': list})

def conference_details(request, pk):
    try :
        conference = Conference.objects.get(conference_id=pk)
        # SELECT * FROM conference WHERE id = pk
    except Conference.DoesNotExist:
        # Handle the case where the conference is not found
        # return render(request, 'conferences/conference_not_found.html', status=404)
        return HttpResponse("Conference not found", status=404)
    return render(request, 'conferences/conference_details.html', {'conference': conference})

def conference_delete(request, pk):
    try:
        conference = Conference.objects.get(conference_id=pk)
        conference.delete()
    # DELETE FROM conference WHERE conference_id = pk
    except Conference.DoesNotExist:
        return render(request, 'conferences/conference_not_found.html', status=404)
    # return HttpResponse("Conference deleted successfully")
    return redirect('conference_list', message="Conference deleted successfully")

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
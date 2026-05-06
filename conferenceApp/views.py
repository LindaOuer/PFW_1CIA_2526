from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy

from .forms import ConferenceFormModel
from .models import Conference


class ConferenceCreateView(CreateView):
    model = Conference
    fields = "__all__"
    # fields = ['name', 'location', 'start_date', 'end_date', 'description', 'theme']
    template_name = "conferences/conference_form.html"
    success_url = reverse_lazy("conference_list")
    form = ConferenceFormModel


# Create your views here.
def conference_list(request):
    list = Conference.objects.all().order_by("-start_date")
    # SELECT * FROM conference ORDER BY start_date DESC
    return render(request, "conferences/conference_list.html", {"conferences": list})


class ConferenceListView(ListView):
    model = Conference
    template_name = "conferences/conference_list.html"
    context_object_name = "conferences"


def conference_details(request, pk):
    try:
        conference = Conference.objects.get(conference_id=pk)
        # SELECT * FROM conference WHERE id = pk
    except Conference.DoesNotExist:
        # Handle the case where the conference is not found
        # return render(request, 'conferences/conference_not_found.html', status=404)
        return HttpResponse("Conference not found", status=404)
    return render(
        request, "conferences/conference_details.html", {"conference": conference}
    )


class ConferenceDetailsView(DetailView):
    model = Conference
    template_name = "conferences/conference_details.html"
    context_object_name = "conference"


def conference_delete(request, pk):
    try:
        conference = Conference.objects.get(conference_id=pk)
        conference.delete()
    # DELETE FROM conference WHERE conference_id = pk
    except Conference.DoesNotExist:
        return render(request, "conferences/conference_not_found.html", status=404)
    # return HttpResponse("Conference deleted successfully")
    return redirect("conference_list", message="Conference deleted successfully")


class ConferenceDeleteView(DeleteView):
    model = Conference
    template_name = "conferences/conference_confirm_delete.html"
    success_url = reverse_lazy("conference_list")


def home(request):
    return render(request, "conferences/home.html")


def name(request, n):
    students = {
        "st1": {"name": "Alice"},
        "st2": {"name": "Bob"},
    }
    return render(
        request,
        "conferences/name.html",
        {"name": "1CIA", "pathVar": n, "students": students},
    )

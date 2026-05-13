from urllib import request

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import ConferenceFormModel, SubmissionFormModel
from .models import Conference, OrganizingCommittee, Submission

def is_participant(user):
    if not user.is_authenticated:
        return False
    print(user.role)
    return user.role == 'participant'

@login_required
@user_passes_test(is_participant, login_url='login')
def submissionRegister(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    form = SubmissionFormModel()
    if request.method == 'POST':
        form = SubmissionFormModel(request.POST, request.FILES)

        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.conference = conference
            submission.save()
            return redirect("conference_details", conference.conference_id)
        else:
            print(form.errors)  
    return render(request, "conferences/submission_form.html", {"form": form, "conference": conference})


class SubmissionCreateView(LoginRequiredMixin, CreateView):
    model = Submission
    form_class = SubmissionFormModel
    template_name = "conferences/submission_form.html"

    def dispatch(self, request, *args, **kwargs):
        # Only participants are allowed
        if request.user.is_authenticated and request.user.role != 'participant':
            return redirect('conference_list')
        self.conference = get_object_or_404(Conference, pk=self.kwargs['conference_id'])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # we add conference to context so that we can access it in the template
        context = super().get_context_data(**kwargs)
        context['conference'] = self.conference
        return context

    def form_valid(self, form):
        # we save the form without commiting it first to set the user and conference
        submission = form.save(commit=False)
        submission.user = self.request.user
        submission.conference = self.conference
        submission.save()
        return redirect('conference_details', pk=self.conference.conference_id)


class SubmissionListView(ListView):
    model = Submission
    template_name = "conferences/submission_list.html"
    context_object_name = "submissions"
    
    def get_queryset(self):
        self.user = self.request.user
        return Submission.objects.filter(user=self.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        return context


def conferenceComitteeList(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    
    comittee = OrganizingCommittee.objects.filter(conference=conference)
    # Accessing using queryset filter to get all OrganizingCommittee objects related to the conference
    # comittee = conference.organized_conferences.all()
    # Accessing the related OrganizingCommittee objects through the conference's related_name 'committees'
    
    return render(request, "conferences/committee_list.html", {"comittee": comittee, "conference": conference})


class CommitteeListView(ListView):
    model = OrganizingCommittee
    template_name = "conferences/committee_list.html"
    context_object_name = "comittee"
    
    def get_queryset(self):
        self.conference = get_object_or_404(Conference, pk=self.kwargs['conference_id'])
        return OrganizingCommittee.objects.filter(conference=self.conference)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conference'] = self.conference
        return context


class ConferenceCreateView(CreateView):
    model = Conference
    fields = ["name", "location", "start_date", "end_date", "description", "theme"]

    # fields = ['name', 'location', 'start_date', 'end_date', 'description', 'theme']
    template_name = "conferences/conference_form.html"
    success_url = reverse_lazy("conference_list")
    # success_url = '/conferenceApp/conferences/'
    form = ConferenceFormModel

    
class ConferenceUpdateView(UpdateView):
    model = Conference
    fields = ["name", "location", "start_date", "end_date", "description", "theme"]
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

@login_required
def conference_delete(request, pk):
    try:
        conference = Conference.objects.get(conference_id=pk)
        conference.delete()
    # DELETE FROM conference WHERE conference_id = pk
    except Conference.DoesNotExist:
        return render(request, "conferences/conference_not_found.html", status=404)
    # return HttpResponse("Conference deleted successfully")
    return redirect("conference_list", message="Conference deleted successfully")


class ConferenceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Conference
    template_name = "conferences/conference_confirm_delete.html"
    success_url = reverse_lazy("conference_list")
    
    def test_func(self):
          return self.request.user.role == 'committee'
    #   return self.request.user.role == 'committee' or self.request.user.is_superuser
    #   return self.request.user.role == 'committee' or self.get_object().created_by == self.request.user
    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)

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

from django.urls import path

from .views import CommitteeListView, ConferenceDeleteView, conference_delete, conference_details, name, home, conference_list, ConferenceListView,  ConferenceCreateView, ConferenceUpdateView, conferenceComitteeList, submissionRegister, SubmissionCreateView, SubmissionListView

urlpatterns = [
    path("", home, name="conference_home"),
    path("name/<str:n>", name, name="conference_name"),
    path("list/", conference_list, name="conference_list"),
    path("details/<int:pk>/", conference_details, name="conference_details"),
    path("delete/<int:pk>/", ConferenceDeleteView.as_view(), name="conference_delete"),
    path("listview/", ConferenceListView.as_view(), name="conference_listview"),
    path('create/', ConferenceCreateView.as_view(), name='conference_create'),
    path('update/<int:pk>/', ConferenceUpdateView.as_view(), name='conference_update'),
    path('committees/<int:conference_id>/', conferenceComitteeList, name='conference_committees_list'),
    path('committees/<int:conference_id>/list/', CommitteeListView.as_view(), name='conference_committees_listview'),
    path('conferences/<int:conference_id>/submit/', submissionRegister, name='submission_register'),
    path('conferences/<int:conference_id>/submitview/', SubmissionCreateView.as_view(), name='submission_createview'),
    path('conferences/Mysubmissions/', SubmissionListView.as_view(), name='submission_listview'),
]

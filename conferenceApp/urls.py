from django.urls import path

from .views import conference_delete, conference_details, name, home, conference_list, ConferenceListView,  ConferenceCreateView

urlpatterns = [
    path("", home, name="conference_home"),
    path("name/<str:n>", name, name="conference_name"),
    path("list/", conference_list, name="conference_list"),
    path("details/<int:pk>/", conference_details, name="conference_details"),
    path("delete/<int:pk>/", conference_delete, name="conference_delete"),
    path("listview/", ConferenceListView.as_view(), name="conference_listview"),
    path('create/', ConferenceCreateView.as_view(), name='conference_create'),
]

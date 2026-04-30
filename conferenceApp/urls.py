from django.urls import path

from .views import conference_delete, conference_details, name, home, conference_list

urlpatterns = [
    path("", home, name="conference_home"),
    path("name/<str:n>", name, name="conference_name"),
    path("list/", conference_list, name="conference_list"),
    path("details/<int:pk>/", conference_details, name="conference_details"),
    path("delete/<int:pk>/", conference_delete, name="conference_delete"),
]

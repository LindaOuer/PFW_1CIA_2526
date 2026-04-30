from django.urls import path

from .views import name, home, conference_list

urlpatterns = [
    path("", home, name="conference_home"),
    path("name/<str:n>", name, name="conference_name"),
    path("list/", conference_list, name="conference_list"),
]

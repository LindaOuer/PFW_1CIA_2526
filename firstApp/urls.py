from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClasseViewSet, ClasseListCreateView

router = DefaultRouter()
router.register(r'classes', ClasseViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("classesAPI", ClasseListCreateView.as_view(), name="classes_api"),
]

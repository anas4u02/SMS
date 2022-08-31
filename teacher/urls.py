from .views import teacherOps
from django.urls import path

urlpatterns = [
    path("teachers/<str:pk>",teacherOps.as_view()),
    path("teachers/",teacherOps.as_view()),
]

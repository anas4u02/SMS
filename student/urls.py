from django.urls import path
from .views import *

urlpatterns = [
    path("students/<str:pk>",studentOps.as_view()),
    path("students/",studentOps.as_view()),
    path("students2/",ClassView.as_view()),

]

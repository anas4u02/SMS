from django.urls import path

from classes.views import ClassView

urlpatterns = [
    path("classes/<str:pk>",ClassView.as_view()),
    path("classes/",ClassView.as_view())
]

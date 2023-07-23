from django.urls import path

from . import views

urlpatterns = [path("", views.Home.as_view()),
            path("homework/", views.HomeWork.as_view()),
            path("homework2/", views.HomeWork2.as_view()),
            path("homework3/", views.HomeWork3.as_view())]


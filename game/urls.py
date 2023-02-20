from django.urls import path
from game import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [path("app1", views.AppIP.as_view()), path("game", views.Game.as_view())]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.resturant_view, name = "resturant-view"),
]
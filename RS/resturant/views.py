from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def resturant_view(request):
    return HttpResponse("This is resturant main page")
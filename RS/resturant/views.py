from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date
from .models import Menu, FoodItem
from django.core import serializers


# Create your views here.

def resturant_view(request):
    return render(request, "resturant/index.html")

def get_breakfast(request):
    menu = Menu.objects.filter(startDate__date = date.today())
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='b'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})

def get_main_course(request):
    menu = Menu.objects.filter(startDate__date = date.today())
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='m'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})

def get_cold_beverage(request):
    menu = Menu.objects.filter(startDate__date = date.today())
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='c'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})


def get_hot_beverage(request):
    menu = Menu.objects.filter(startDate__date = date.today())
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='h'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})


def get_dessert(request):
    menu = Menu.objects.filter(startDate__date = date.today())
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='d'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})

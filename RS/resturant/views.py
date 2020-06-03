from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date
from .models import Menu, FoodItem
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import json


# Create your views here.

def resturant_view(request):
    return render(request, "resturant/index.html")

def get_breakfast(request):
    menu = Menu.objects.filter(pk=7)
    print(menu)
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='b'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})

def get_main_course(request):
    menu = Menu.objects.filter(pk=7)
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='m'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})

def get_cold_beverage(request):
    menu = Menu.objects.filter(pk=7)
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='c'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})


def get_hot_beverage(request):
    menu = Menu.objects.filter(pk=7)
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='h'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})


def get_dessert(request):
    menu = Menu.objects.filter(pk=7)
    if menu:
        foodItems = list(menu[0].FoodItems.filter(category='d'))
        foodItem_json = serializers.serialize('json', foodItems)
        return HttpResponse(foodItem_json)
    else:
        return HttpResponse({'error':'empty'})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if (list(User.objects.filter(username = username)) != []):
            return HttpResponse(json.dumps({"status":False, "error":"Username already exist !", "target":"#usernameregerror"}))
        if (list(User.objects.filter(email = email)) != []):
            return HttpResponse(json.dumps({"status":False, "error":"Email already exist !", "target":"#emailregerror"}))
        if (len(password) < 8):
            return HttpResponse(json.dumps({"status":False, "error":"Password must contain atleast 8 characters !", "target":"#passwordregerror"}))
        
        user = User.objects.create_user(username, email, password)
        user.first_name  = firstname
        user.last_name = lastname
        user.save()

        return HttpResponse(json.dumps({"status":True}))
    else:
        return HttpResponse(json.dumps({"status":False, "error":"", "target":""}))


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if (list(User.objects.filter(username = username)) == []):
           return HttpResponse(json.dumps({"status":False, "error":"Invalid Username or Password", "target":"#logerror"}))
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse(json.dumps({"status":True, "error":"", "target":"", "user":user.username}))
            else:
                return HttpResponse(json.dumps({"status":False, "error":"Invalid Username or Password", "target":"#logerror"}))
    else:
        return HttpResponse(json.dumps({"status":False, "error":"", "target":""}))

def logout_v(request):
    user = request.user.username
    logout(request)
    return HttpResponse(json.dumps({"status":True, "user":user}))

def user_auth(request):
    if request.user.is_authenticated:
        usr = {"auth":True, "user":request.user.username}
        return HttpResponse(json.dumps(usr))
    else:
        usr = {"auth":False}
        return HttpResponse(json.dumps(usr))

    
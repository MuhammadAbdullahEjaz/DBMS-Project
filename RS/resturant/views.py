from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import date
from .models import Menu, FoodItem, UserCart, Cart, Order, OrderItem
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
        cart =  UserCart.objects.create(user_id = user)
        cart.save()
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


def add_to_c(request):
    if request.method == 'POST' and request.user.is_authenticated:
        item_id = request.POST.get('item_id')
        food = list(FoodItem.objects.filter(pk = item_id))
        usercart = list(UserCart.objects.filter(user_id = request.user))

        if (usercart and food):
            cart = list(Cart.objects.filter(cart_id= usercart[0], food_id = food[0]))
            if cart:
                if cart[0].quantity > 0 and cart[0].quantity < 6:
                    cart[0].quantity += 1
                    cart[0].save()
                else:
                    return HttpResponse(json.dumps({"status":False, "max":True}))
            else:
                Cart.objects.create(cart_id = usercart[0], food_id = food[0] , quantity = 1)
            return HttpResponse(json.dumps({"status":True, "max":False}))
    else:
        return HttpResponse(json.dumps({"status":False, "max":False}))

def get_c(request):
    if request.user.is_authenticated:
        user = request.user
        usercart = list(UserCart.objects.filter(user_id = user))
        user_items = list(Cart.objects.filter(cart_id = usercart[0]))
        c =list()
        price = 0.0
        for i in user_items:
            i_name = i.food_id.name
            i_price = i.food_id.Price
            i_quantity = i.quantity
            price += float(i_price)*i_quantity
            d = dict(item_name = i.food_id.name, item_price = float(i.food_id.Price), item_quantity = i_quantity, item_cart = i.id)
            c.append(d)
        context = {"status": True,"error":"" ,"user_items":c, "amount":price}
        if user_items:
            return HttpResponse(json.dumps(context))
        else:
            return HttpResponse(json.dumps({"status":True, "error":"No Item In the Cart"}))
        #serializers.serialize('json', user_items)
    else:
        return HttpResponse(json.dumps({"status":False}))

def remove_item_from_cart(request):
    if request.user.is_authenticated and request.method == 'POST':
        cart_id = request.POST.get("cart_id")
        user = request.user
        usercart = list(UserCart.objects.filter(user_id = user))
        cart = list(Cart.objects.filter(pk=cart_id))
        if cart:
            if (cart[0].cart_id.id == usercart[0].id):
                price = float(cart[0].food_id.Price)
                quantity = cart[0].quantity
                price_t = price * quantity
                cart[0].delete()
                return HttpResponse(json.dumps({"status":True, "amount":price_t}))
            else:
                return HttpResponse(json.dumps({"status":False}))
        else:
            return HttpResponse(json.dumps({"status":False}))
    else:
        return HttpResponse(json.dumps({"status":False}))
def neg_q(request):
    if request.user.is_authenticated and request.method == 'POST':
        user = request.user
        cart_id = request.POST.get('cart_id')
        usercart = list(UserCart.objects.filter(user_id = user))
        cart = list(Cart.objects.filter(pk=cart_id))
        if cart:
            if (cart[0].cart_id.id == usercart[0].id and cart[0].quantity > 1):
                cart[0].quantity -= 1
                cart[0].save()
                return HttpResponse(json.dumps({"status":True, "item_quantity":cart[0].quantity, "amount":float(cart[0].food_id.Price)}))
            else:
                return HttpResponse(json.dumps({"status":False}))
        else:
            return HttpResponse(json.dumps({"status":False}))
    else:
        return HttpResponse(json.dumps({"status":False}))

def pos_q(request):
    if request.user.is_authenticated and request.method == 'POST':
        user = request.user
        cart_id = request.POST.get('cart_id')
        usercart = list(UserCart.objects.filter(user_id = user))
        cart = list(Cart.objects.filter(pk=cart_id))
        if cart:
            if (cart[0].cart_id.id == usercart[0].id and cart[0].quantity < 6):
                cart[0].quantity += 1
                cart[0].save()
                return HttpResponse(json.dumps({"status":True, "item_quantity":cart[0].quantity, "amount":float(cart[0].food_id.Price)}))
            else:
                return HttpResponse(json.dumps({"status":False}))
        else:
            return HttpResponse(json.dumps({"status":False}))
    else:
        return HttpResponse(json.dumps({"status":False}))

def order(request):
    if request.user.is_authenticated and request.method == 'POST':
        cart_id = list(UserCart.objects.filter(user_id = request.user))
        if(cart_id):
            cart_q = Cart.objects.filter(cart_id = cart_id[0])
            cart = list(cart_q)
            if cart:
                new_order = Order.objects.create(user_id = request.user, total_price= 0)
                new_order.save()
                price = 0
                for i in cart:
                    OrderItem.objects.create(order_id = new_order, food_id = i.food_id, quantity= i.quantity)
                    price += i.food_id.Price*i.quantity
                    new_order.total_price = price
                new_order.save()
                cart_q.delete()
                return HttpResponse(json.dumps({"status":True}))
            else:
                return HttpResponse(json.dumps({"status":False}))
        else:
            return HttpResponse(json.dumps({"status":False}))
    else:
        return HttpResponse(json.dumps({"status":False}))
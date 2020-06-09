from django.contrib import admin
from .models import FoodItem, Menu, UserCart, Cart, Order, OrderItem
# Register your models here.
admin.site.register(FoodItem)
admin.site.register(Menu)
admin.site.register(UserCart)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
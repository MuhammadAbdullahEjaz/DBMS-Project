from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class FoodItem(models.Model):
    name = models.CharField(max_length=20, null = False, blank = False)
    Price = models.DecimalField(max_digits = 6, decimal_places = 2)

    CATEGORY_OPT = (
        ('b','Breakfast'),
        ('m','Main Course'),
        ('c','Cold Beverage'),
        ('h','Hot Beverage'),
        ('d','Dessert'),
    )

    category = models.CharField(max_length = 1, choices = CATEGORY_OPT, default = 'm')
    serving  = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'

class Menu(models.Model):
    startDate = models.DateTimeField(auto_now = True)
    endDate = models.DateTimeField()
    FoodItems = models.ManyToManyField(FoodItem, related_name = 'Food') 

    def __str__(self):
        return f'{self.startDate} -- {self.endDate}'
    

class UserCart(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name="usercart")

    def __str__(self):
        return f"{self.user_id.username} -- {self.id}"

class Cart(models.Model):
    cart_id = models.ForeignKey(UserCart, on_delete = models.CASCADE)
    food_id = models.ForeignKey(FoodItem, on_delete = models.CASCADE)
    quantity = models.IntegerField(validators = [MaxValueValidator(6), MinValueValidator(1)])

    def __str__(self):
        return f"{self.cart_id} = ({self.food_id} | {self.quantity})"
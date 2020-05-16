from django.db import models

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
        return f'{self.name} - {self.category}'

class Menu(models.Model):
    startDate = models.DateTimeField(auto_now = True)
    endDate = models.DateTimeField()
    FoodItems = models.ManyToManyField(FoodItem, related_name = 'Food') 

    def __str__(self):
        food = self.FoodItems.all()
        items = ''
        for f in food:
            items += f'{f}' + ' | '
        return items
    

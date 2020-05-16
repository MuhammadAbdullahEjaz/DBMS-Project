# Generated by Django 3.0.6 on 2020-05-16 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.CharField(choices=[('b', 'Breakfast'), ('m', 'Main Course'), ('c', 'Cold Beverage'), ('h', 'Hot Becerage'), ('d', 'Dessert')], default='m', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateTimeField(auto_now=True)),
                ('endDate', models.DateTimeField()),
                ('FoodItems', models.ManyToManyField(related_name='Food', to='resturant.FoodItem')),
            ],
        ),
    ]

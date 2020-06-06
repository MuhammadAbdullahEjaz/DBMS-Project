# Generated by Django 3.0.6 on 2020-06-05 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resturant', '0003_usercart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturant.UserCart')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resturant.FoodItem')),
            ],
        ),
    ]
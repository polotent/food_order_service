from django.db import models


class MenuItem(models.Model):
    pass

class Menu(models.Model):
    menu_name = models.CharField(max_length=200)


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)


class Order(models.Model):
    pass

class OrderItem(models.Model):
    pass
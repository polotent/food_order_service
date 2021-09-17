from django.db import models


class Menu(models.Model):
    menu_name = models.CharField(max_length=200)


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_price = models.IntegerField(default=0)


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)


class Order(models.Model):
    order_date = models.DateTimeField()
    order_restaurant = models.ForeignKey(
        Restaurant, on_delete=models.DO_NOTHING
    )
    order_user_addr = models.CharField(max_length=200)
    order_user_phone = models.CharField(max_length=200)
    order_status = models.CharField(max_length=200)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    menu_item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    order_item_price = models.IntegerField(default=0)
    order_item_quantity = models.IntegerField(default=0)

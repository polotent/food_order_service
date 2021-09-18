from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('restaurants', views.restaurants, name='restaurants'),
    path('menu', views.menu, name='menu'),
    path('preorder', views.preorder, name='preorder'),
    path('order', views.order, name='order')
]

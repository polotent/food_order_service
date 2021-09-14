from django.urls import path

from . import views

urlpatterns = [
    path('restaurants', views.restaurants, name='restaurants_list'),
    path('<int:restaurant_id>/menu', views.menu, name='items_list'),
    path('order', views.order, name='order')
]
from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('restaurants', views.restaurants, name='restaurants'),
    path('<int:menu_id>/menu', views.menu, name='menu'),
    path('order', views.order, name='order')
]

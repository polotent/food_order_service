from django.http import JsonResponse
from django.db import DatabaseError
from .models import Item, Restaurant, Menu
import logging


def restaurants(request):
    """
    Return JsonResponse with list of restaurants.
    """
    response = dict()
    try:
        response['restaurants'] = list(
            Restaurant.objects.values('restaurant_name', 'menu_id')
        )
    except DatabaseError as e:
        response = {'error': 'Error during db transaction'}
        logging.info(f'\"{request.path}\" Error during db transaction: {e}')
    logging.info(f'\"{request.path}\" Sending response: {response}')
    return JsonResponse(response)


def menu(request):
    """
    Return JsonResponse with name of menu
    and items for specified restaurant.
    """
    data = request
    print(data['asdasd'])
    menu_id = data['menu_id']
    response = dict()
    try:
        menu_qs = Menu.objects.filter(pk=menu_id).first()
    except DatabaseError as e:
        response = {'error': 'Error during db transaction'}
        logging.info(f'\"{request.path}\" Error during db transaction: {e}')
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if not menu_qs:
        response['error'] = 'Menu not found with requested id'
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    response['menu_name'] = menu_qs.menu_name

    try:
        menu_items = list(
            Item.objects.filter(
                menu=menu_qs.id
            ).values(
                'id', 'item_name', 'item_price'
            )
        )
    except DatabaseError as e:
        response = {'error': 'Error during db transaction'}
        logging.info(f'\"{request.path}\" Error during db transaction: {e}')
        logging.info(f'\"{request.path}\" Sending response: {response}')

    response['menu_items'] = menu_items

    logging.info(f'\"{request.path}\" Sending response: {response}')
    return JsonResponse(response)


def order(request):
    response = dict()
    return JsonResponse(response)

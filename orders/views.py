from django.http import JsonResponse
from django.db import DatabaseError
from .models import Item, Restaurant, Menu, Order, OrderItem
import logging
import json
from datetime import datetime

from .helpers import calc_total_price


def restaurants(request):
    """
    Return JsonResponse with list of restaurants.
    """
    response = dict()

    if request.method != 'POST':
        response = {'error': 'Request method must be POST'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

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
    response = dict()

    if request.method != 'POST':
        response = {'error': 'Request method must be POST'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    try:
        request_data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        response = {'error': 'Wrong data format'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    menu_id = request_data.get('menu_id')

    if not menu_id:
        response = {'error': 'Missing id parameter for menu'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if type(menu_id) != int:
        response = {'error': 'Menu menu_id parameter must be int type'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    try:
        menu_qs = Menu.objects.filter(pk=menu_id).first()
    except DatabaseError as e:
        response = {'error': 'Error during db transaction'}
        logging.info(f'\"{request.path}\" Error during db transaction: {e}')
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if not menu_qs:
        response = {'error': 'Menu not found with requested id'}
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


def preorder(request):
    """
    Specify menu_items and their quantity
    for the order. Return JsonResponse containing
    total price for all menu_items and order id.
    """
    response = dict()

    if request.method != 'POST':
        response = {'error': 'Request method must be POST'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    try:
        request_data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        response = {'error': 'Wrong data format'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    item_list = request_data.get('items')
    if not item_list:
        response = {'error': 'Item list is empty'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if type(item_list) != list:
        response = {'error': 'Items must be represented as a list'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    for item in item_list:
        if type(item) != dict:
            response = {'error': 'Wrong request format'}
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        item_id = item.get('id')
        item_quantity = item.get('quantity')

        if not item_id:
            response = {'error': 'Missing id parameter for item'}
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        if type(item_id) != int:
            response = {'error': 'Item id parameter must be int type'}
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        if not item_quantity and item_quantity != 0:
            response = {'error': 'Missing quantity parameter for item'}
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        if type(item_quantity) != int:
            response = {'error': 'Item quantity parameter must be int type'}
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        if item_quantity <= 0:
            response = {
                'error': f'Item quantity parameter must be positive, {item_quantity} was given'
            }
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        try:
            item_qs = Item.objects.filter(pk=item_id).first()
        except DatabaseError as e:
            response = {'error': 'Error during db transaction'}
            logging.info(
                f'\"{request.path}\" Error during db transaction: {e}'
            )
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        if not item_qs:
            response = {'error': 'Item not found with requested id'}
            logging.info(f'\"{request.path}\" Sending response: {response}')
            return JsonResponse(response)

        item['price'] = item_qs.item_price
        item['qs'] = item_qs

    total_price = calc_total_price(item_list)
    response['total_price'] = total_price

    order = Order(
        order_date=datetime.now(),
        order_total_price=total_price,
        order_status='registration'
    )
    order.save()

    response['order_id'] = order.id

    for item in item_list:
        order_item = OrderItem(
            order=order,
            menu_item=item['qs'],
            order_item_price=item['price'],
            order_item_quantity=item['quantity']
        )
        order_item.save()

    return JsonResponse(response)


def order(request):
    """
    Finilize order, specifying address
    and phone number. This is done
    after preordering.
    """
    response = dict()

    if request.method != 'POST':
        response = {'error': 'Request method must be POST'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    try:
        request_data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        response = {'error': 'Wrong data format'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    order_id = request_data.get('order_id')
    user_addr = request_data.get('user_addr')
    user_phone = request_data.get('user_phone')

    if not order_id:
        response = {'error': 'Missing id parameter for order'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if type(order_id) != int:
        response = {'error': 'Order id parameter must be int type'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if not user_addr:
        response = {'error': 'Missing user_addr parameter for order'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if type(user_addr) != str:
        response = {'error': 'Order user_addr parameter must be int type'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if not user_phone:
        response = {'error': 'Missing user_phone parameter for order'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if type(user_phone) != str:
        response = {'error': 'Order user_phone parameter must be int type'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    try:
        order_qs = Order.objects.filter(pk=order_id).first()
    except DatabaseError as e:
        response = {'error': 'Error during db transaction'}
        logging.info(
            f'\"{request.path}\" Error during db transaction: {e}'
        )
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    if not order_qs:
        response = {'error': 'Order not found with requested id'}
        logging.info(f'\"{request.path}\" Sending response: {response}')
        return JsonResponse(response)

    

    return JsonResponse(response)

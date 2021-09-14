from django.http import JsonResponse
from .models import Restaurant


def restaurants(request):
    response = dict()
    return JsonResponse(response)


def menu(request):
    response = dict()
    return JsonResponse(response)


def order(request):
    response = dict()
    return JsonResponse(response)

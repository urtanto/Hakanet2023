"""
view functions
"""
# from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest

from main.models import User


def get_name(x: User) -> str:
    return x.username


def start_page(request: WSGIRequest) -> JsonResponse:
    """function of starting page"""
    users = list(map(get_name, User.objects.all()))
    context = {
        "text": "starting page",
        "users": users
    }
    return JsonResponse(context)

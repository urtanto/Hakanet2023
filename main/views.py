"""
view functions
"""
# from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest


def start_page(request: WSGIRequest) -> JsonResponse:
    """function of starting page"""
    context = {
        "text": "starting page"
    }
    return JsonResponse(context)

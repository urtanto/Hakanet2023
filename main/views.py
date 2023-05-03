"""
view functions
"""
# from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.hashers import make_password
from main.models import User


def get_name(x: User) -> str:
    return x.username


@ensure_csrf_cookie
def auth_set_csrf_cookie(request):
    return JsonResponse({"details": "CSRF cookie set"})


def registration(request: WSGIRequest) -> JsonResponse:
    if request.method == "POST":
        user = User(username=request.POST['username'],
                    password=make_password(request.POST['password']),
                    email=request.POST['email'])
        user.save()
        return JsonResponse({"text": "ok"})
    return JsonResponse({"error"})


def start_page(request: WSGIRequest) -> JsonResponse:
    """function of starting page"""
    users = list(map(get_name, User.objects.all()))
    context = {
        "text": "starting page",
        "users": users,
    }
    return JsonResponse(context)

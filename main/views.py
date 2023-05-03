"""
view functions
"""
# from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.hashers import make_password
from main.models import User

from PIL import Image
from main.models import User, Photo


def get_name(x: User) -> str:
    return x.username


def get_image_path(x: Photo) -> list:
    return [x.photo_before, x.photo_after]


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


def photo_sort(request: WSGIRequest) -> JsonResponse:
    type_of_product = request.GET["product"]
    type_of_stuff = request.GET["stuff"]
    type_of_time = request.GET["time"]
    level_of_dirt = request.GET["dirt"]

    all_photos_objective = Photo.objects.filter(type_of_product=type_of_product,
                                                type_of_time=type_of_time,
                                                level_of_dirt=level_of_dirt,
                                                type_of_stuff=type_of_stuff)

    all_photos = list(map(get_image_path, all_photos_objective))
    content = []
    for [path1, path2] in all_photos:
        img1 = open(path1, "rb").read()
        img2 = open(path2, "rb").read()
        content.append([img1, img2])

    context = {
        "photos": content
    }

    return JsonResponse(context)

"""
view functions
"""
from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.hashers import make_password
from main.models import User

from main.models import User, Photo, Article


def get_name(x: User) -> str:
    return x.username


def get_image_path(x: Photo) -> list:
    return [x.photo_before, x.photo_after]


def get_names_of_articles(x: Article) -> list:
    return [x.name, x.id]


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


@login_required
def check(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({"text": "okkkkk"})


def get_all_articles(request: WSGIRequest):
    content = list(map(get_names_of_articles, Article.objects.all()))

    context = {
        "names": content
    }

    return JsonResponse(context)


def get_one_article(request: WSGIRequest):
    id = request.GET["id"]

    article = Article.objects.filter(id=id)[0]
    name = article.name
    text = article.text

    context = {
        "text": text,
        "name": name
    }

    return JsonResponse(context)


def get_comments_for_article(request: WSGIRequest):
    name = request.GET["name"]

    id = Article.objects.filter(name=name)[0].id
    comments_objective = Article.objects.get(name=name).commentforarticle_set.all()

    comments = []
    for i in comments_objective:
        comment_user = i.user.username
        comment_text = i.text
        comments.append([comment_user, comment_text])

    context = {
        "comments": comments
    }

    return JsonResponse(context)


def make_article(request: WSGIRequest):
    text = request.POST["text"]
    name = request.POST["name"]

    new_article = Article(text=text, name=name)
    new_article.save()

    context = {
        "ok": "ok"
    }

    return JsonResponse(context)

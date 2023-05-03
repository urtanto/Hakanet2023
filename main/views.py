from django.core.handlers.wsgi import WSGIRequest
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from Hakanet2023.serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from main.models import User, Photo, Article


def get_token(request: WSGIRequest) -> str:
    return request.headers.get("Authorization").split()[1]


def need_login(method: list):
    """
    simple decorator
    :param method: GET/POST
    :return: func
    """

    def need_login_decorator(func):
        @api_view(method)
        @authentication_classes([SessionAuthentication, TokenAuthentication])
        @permission_classes([IsAuthenticated])
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapped

    return need_login_decorator


def get_name(x: User) -> str:
    """
    function getting user's name
    """
    return x.username


def get_image_path(x: Photo) -> list:
    """
    function getting path of 2 images
    """
    return [x.photo_before, x.photo_after]


def get_names_of_articles(x: Article) -> str:
    return x.name


def start_page(request: WSGIRequest) -> Response:
    """
    function of starting page
    """
    users = list(map(get_name, User.objects.all()))
    context = {
        "text": "starting page",
        "users": users,
    }
    return Response(context)


def photo_sort(request: WSGIRequest) -> Response:
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

    return Response(context)


def get_all_articles(request: WSGIRequest) -> Response:
    content = list(map(get_names_of_articles, Article.objects.all()))

    context = {
        "names": content
    }

    return Response(context)


def get_one_article(request: WSGIRequest) -> Response:
    name = request.GET["name"]

    text = Article.objects.filter(name=name)[0].text

    context = {
        "text": text
    }

    return Response(context)


def get_comments_for_article(request: WSGIRequest) -> Response:
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

    return Response(context)


def make_article(request: WSGIRequest) -> Response:
    text = request.POST["text"]
    name = request.POST["name"]

    new_article = Article(user=1, text=text, name=name)
    new_article.save()

    return Response("ok")


@api_view(["POST"])
def signup(request: WSGIRequest) -> Response:
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = get_user_model().objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request) -> Response:
    user = get_object_or_404(get_user_model(), username=request.data["username"])
    if not user.check_password(request.data["password"]):
        return Response({"detail": "Bad password"}, status=status.HTTP_400_BAD_REQUEST)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


@need_login(["GET"])
def test(request: WSGIRequest) -> Response:
    return Response(f"passed for {request.user.username}")


@need_login(["POST"])
def logout(request):
    Token.objects.get(user=request.user).delete()
    return Response("logout")


@need_login(["GET"])
def get_user(request):
    print(request.user.__dict__)
    user = {}
    waste_keys = [
        "id",
        "_state",
        "password",
        "super_user",
        "is_staff",
    ]
    for key in request.user.__dict__:
        if key not in waste_keys:
            user[key] = request.user.__dict__[key]
    return Response({"user": user})

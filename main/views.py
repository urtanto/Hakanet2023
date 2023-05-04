from django.core.files.storage import FileSystemStorage
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from Hakanet2023.serializers import UserSerializer

from main.models import User, Photo, Article, StuffType, TimeType, DirtType, ProductType


def need_login(method: list):
    """
    simple decorator collected 3 other decorators
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


def get_token(request: WSGIRequest) -> str:
    """
    Getting authorization token from request
    :param request: request with token
    :return: only token
    """
    return request.headers.get("Authorization").split()[1]


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


def get_names_of_articles(x: Article) -> list:
    return [x.name, x.id]


@api_view(["GET"])
def start_page(request: WSGIRequest) -> Response:
    return Response("Hello")


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


@need_login(["POST"])
def logout(request):
    Token.objects.get(user=request.user).delete()
    return Response("successful")


@api_view(["GET"])
def get_main_page(request: WSGIRequest) -> Response:
    context = {"services": [
        {
            "name": "first",
            "cost": 2050.20,
            "description": "da " * 100
        },
        {
            "name": "second",
            "cost": 4450.55,
            "description": "net " * 100
        },
    ],
        "comments": [
            {
                "user": {
                    "username": "da",
                    "first_name": "A.",
                    "second_name": "B",
                    "picture": open("static/images/default.png", "rb").read()
                },
                "comment": "some text" * 50
            }
        ]
    }
    return Response(context)


@api_view(["GET"])
def get_services(request: WSGIRequest) -> Response:
    context = {"services": [
        {
            "name": "first",
            "cost": 2050.20,
            "description": "da " * 100
        },
        {
            "name": "second",
            "cost": 4450.55,
            "description": "net " * 100
        },
    ]
    }
    return Response(context)


@api_view(["GET"])
def get_service(request: WSGIRequest, service_id: int) -> Response:
    context = {"services": {
        "service_id": service_id,
        "name": "first",
        "cost": 2050.20,
        "description": "da " * 100
    }
    }
    return Response(context)


@api_view(["GET"])
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


@api_view(["GET"])
def get_all_articles(request: WSGIRequest) -> Response:
    content = list(map(get_names_of_articles, Article.objects.all()))

    context = {
        "names": content
    }

    return Response(context)


@api_view(["GET"])
def get_one_article(request: WSGIRequest) -> Response:
    article_id = request.GET["id"]

    article = Article.objects.filter(id=article_id)[0]
    name = article.name
    text = article.text

    context = {
        "text": text,
        "name": name
    }

    return Response(context)


@api_view(["GET"])
def get_comments_for_article(request: WSGIRequest) -> Response:
    name = request.GET["name"]

    # id = Article.objects.filter(name=name)[0].id
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


@api_view(["POST"])
def make_article(request: WSGIRequest) -> Response:
    text = request.POST["text"]
    name = request.POST["name"]
    new_article = Article(text=text, name=name)
    new_article.save()

    return Response("ok")


@need_login(["GET"])
def test(request: WSGIRequest) -> Response:
    return Response(f"passed for {request.user.username}")


@need_login(["GET"])
def get_user(request):
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


@need_login(["POST"])
def image_upload(request: WSGIRequest) -> Response:
    file = request.FILES['file']
    fs = FileSystemStorage()
    fs.save(file.name, file.file)
    return Response({"filename": file.name})


@need_login(["POST"])
def photo_upload(request: WSGIRequest) -> Response:
    photo = Photo(
        photo_before=request.POST["filename_before"],
        photo_after=request.POST["filename_after"],
        type_of_product="",
        type_of_stuff="",
        type_of_dirt="",
        type_of_time="",
    )
    return Response("saved")


# тут админка get
def get_all_stuff_types(request: WSGIRequest) -> Response:
    all_objective = StuffType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "stuff": all_
    }

    return Response(context)


# тут админка post
def delete_stuff_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = StuffType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
def change_stuff_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type = StuffType.objects.filter(type=before)[0]

    type.type = after

    type.save()

    return Response({"ans": "ok"})


# тут админка get
def get_all_product_types(request: WSGIRequest) -> Response:
    all_objective = ProductType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "product": all_
    }

    return Response(context)


# тут админка post
def delete_product_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = ProductType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
def change_product_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type = ProductType.objects.filter(type=before)[0]

    type.type = after

    type.save()

    return Response({"ans": "ok"})


# тут админка get
def get_all_time_types(request: WSGIRequest) -> Response:
    all_objective = TimeType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "time": all_
    }

    return Response(context)


# тут админка post
def delete_time_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = TimeType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
def change_time_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type = TimeType.objects.filter(type=before)[0]

    type.type = after

    type.save()

    return Response({"ans": "ok"})


# тут админка get
def get_all_dirt_types(request: WSGIRequest) -> Response:
    all_objective = DirtType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "dirt": all_
    }

    return Response(context)


# тут админка post
def delete_dirt_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = DirtType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
def change_dirt_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type = DirtType.objects.filter(type=before)[0]

    type.type = after

    type.save()

    return Response({"ans": "ok"})


def make_new_service(request: WSGIRequest) -> Response:
    type_of_product = request.POST["product"]
    type_of_stuff = request.POST["stuff"]
    type_of_time = request.POST["time"]
    level_of_dirt = request.POST["dirt"]

    return Response({"ans": "ok"})

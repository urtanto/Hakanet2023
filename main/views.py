import os

from django.core.files.storage import FileSystemStorage
from django.template.defaultfilters import register
from django.http import JsonResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from Hakanet2023.serializers import UserSerializer

from Hakanet2023.settings import BASE_DIR
from main.forms import PhotoUploadForm, ProductCreateForm, ProductEditForm
from main.models import User, Photo, Article, StuffType, TimeType, DirtType, CommentForArticle, Order, ReviewForCompany, \
    ProductType


def get_product_type_choices():
    obj = ProductType.objects.all()
    data = []
    for i in range(len(obj)):
        data.append((obj[i].id, obj[i].type))
    return tuple(data)


def get_stuff_type_choices():
    obj = StuffType.objects.all()
    data = []
    for i in range(len(obj)):
        data.append((obj[i].id, obj[i].type))
    return tuple(data)


def get_dirt_type_choices():
    obj = DirtType.objects.all()
    data = []
    for i in range(len(obj)):
        data.append((obj[i].id, obj[i].type))
    return tuple(data)


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


def need_admin(func):
    def wrapped(*args, **kwargs):
        request: WSGIRequest = args[0]
        res = get_admin(request)
        if not res.data["ans"]:
            return JsonResponse({"detail": "you are not admin"}, status=status.HTTP_403_FORBIDDEN)
        return func(*args, **kwargs)

    return wrapped


def front(func):
    def wrapped(*args, **kwargs):
        request: WSGIRequest = args[0]
        user = get_object_or_404(get_user_model(), username=request.GET.get("u", None))
        if not user.check_password(request.GET.get("p")):
            return redirect(reverse("error"))
        return func(*args, **kwargs)

    return wrapped


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
            "service_id": 1,
            "name": "first",
            "cost": 2050.20,
            "description": "da " * 100
        },
        {
            "service_id": 2,
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

    context = {
        "photos": all_photos
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
        comment_id = i.id
        comments.append([comment_user, comment_text, comment_id])

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


def load_image(request: WSGIRequest, name="file"):
    file = request.FILES[name]
    fs = FileSystemStorage()
    filename = f"{len(os.listdir(BASE_DIR / 'main/static/images'))}_{file.name}"
    fs.save(filename, file.file)
    return filename


@need_login(["POST"])
def image_upload(request: WSGIRequest) -> Response:
    filename = load_image(request)
    return Response({"filename": filename})


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


@need_login(["GET", "POST"])
def get_admin(request: WSGIRequest) -> Response:
    return Response({"ans": request.user.super_user})


# тут админка get
@need_admin
@need_login(["GET"])
def get_all_stuff_types(request: WSGIRequest) -> Response:
    all_objective = StuffType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "stuff": all_
    }

    return Response(context)


# тут админка post
@need_admin
@need_login(["POST"])
def delete_stuff_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = StuffType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
@need_admin
@need_login(["GET", "POST"])
def change_stuff_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type = StuffType.objects.filter(type=before)[0]

    type.type = after

    type.save()

    return Response({"ans": "ok"})


# тут админка get
@need_admin
@need_login(["GET"])
def get_all_product_types(request: WSGIRequest) -> Response:
    all_objective = ProductType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "product": all_
    }

    return Response(context)


# тут админка post
@need_admin
@need_login(["POST"])
def delete_product_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = ProductType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
@need_admin
@need_login(["POST"])
def change_product_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type = ProductType.objects.filter(type=before)[0]

    type.type = after

    type.save()

    return Response({"ans": "ok"})


# тут админка get
@need_admin
@need_login(["GET"])
def get_all_time_types(request: WSGIRequest) -> Response:
    all_objective = TimeType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "time": all_
    }

    return Response(context)


# тут админка post
@need_admin
@need_login(["POST"])
def delete_time_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = TimeType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
@need_admin
@need_login(["POST"])
def change_time_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type = TimeType.objects.filter(type=before)[0]

    type.type = after

    type.save()

    return Response({"ans": "ok"})


# тут админка get
@need_admin
@need_login(["GET"])
def get_all_dirt_types(request: WSGIRequest) -> Response:
    all_objective = DirtType.objects.all()

    all_ = list(map(lambda x: x.type, all_objective))

    context = {
        "dirt": all_
    }

    return Response(context)


# тут админка post
@need_admin
@need_login(["POST"])
def delete_dirt_type(request: WSGIRequest) -> Response:
    deleted = request.POST["type"]

    type = DirtType.objects.filter(type=deleted)[0]

    type.delete()

    return Response({"ans": "ok"})


# тут админка post
@need_admin
@need_login(["POST"])
def change_dirt_type(request: WSGIRequest) -> Response:
    before = request.POST["before"]
    after = request.POST["after"]

    type_ = DirtType.objects.filter(type=before)[0]

    type_.type = after

    type_.save()

    return Response({"ans": "ok"})


# тут админка post
@need_admin
@need_login(["POST"])
def delete_comment_for_article(request: WSGIRequest) -> Response:
    id_ = request.POST["id"]

    comment = DirtType.objects.filter(id=id_)[0]

    comment.delete()

    return Response({"ans": "ok"})


# тут юзер post
@need_login(["POST"])
def make_comment_for_article(request: WSGIRequest) -> Response:
    user = request.user
    text = request.POST["text"]
    article_id = request.POST["id"]

    new_com = CommentForArticle(user=user, text=text, article=Article.objects.filter(id=article_id))
    new_com.save()

    return Response({"ans": "ok"})


# тут юзер post
@need_login(["POST"])
def make_review(request: WSGIRequest) -> Response:
    user = request.user
    text = request.POST["text"]

    new_com = ReviewForCompany(user=user, text=text)
    new_com.save()

    return Response({"ans": "ok"})


@register.filter
def is_drop(n):
    return isinstance(n, list)


@register.filter
def get_list(n):
    return n[1:]


def get_menu_context():
    """
    Функция для возвращения контекста меню

    :return: контекст меню
    """
    return [
        {'url_name': 'admin', 'name': 'Меню'},
        [
            "Статьи",
            {'url_name': 'admin', 'name': 'Создавать'},
            {'url_name': 'admin', 'name': 'Редактировать'},
            {'url_name': 'admin', 'name': 'Удалить'},
        ],
        {'url_name': 'photo_upload', 'name': 'Загрузить фото'},
        [
            "Типы Изделия",
            {'url_name': 'product_create', 'name': 'Создать'},
            {'url_name': 'product_view_edit', 'name': 'Редактировать', "action_type": "edit"},
            {'url_name': 'product_view_edit', 'name': 'Удалить', "action_type": "delete"},
        ],
        [
            "Типы Материла",
            {'url_name': 'admin', 'name': 'Создать'},
            {'url_name': 'admin', 'name': 'Редактировать'},
            {'url_name': 'admin', 'name': 'Удалить'},
        ],
        [
            "Типы Загрязненности",
            {'url_name': 'admin', 'name': 'Создавать'},
            {'url_name': 'admin', 'name': 'Редактировать'},
            {'url_name': 'admin', 'name': 'Удалить'},
        ],
        [
            "Типы Срочности",
            {'url_name': 'admin', 'name': 'Создать'},
            {'url_name': 'admin', 'name': 'Редактировать'},
            {'url_name': 'admin', 'name': 'Удалить'},
        ],
        {'url_name': 'admin', 'name': 'Удаление отзывов'},
        {'url_name': 'admin', 'name': 'Удаление коментариев'},
    ]


@front
def admin_start(request: WSGIRequest):
    context = {
        'menu': get_menu_context(),
        'username': request.GET.get("u"),
        'password': request.GET.get("p"),
    }
    return render(request, 'pages/admin_start.html', context)


@front
def admin_photo_upload(request: WSGIRequest):
    context = {
        'menu': get_menu_context(),
        'username': request.GET.get("u"),
        'password': request.GET.get("p"),
    }
    pdt = get_product_type_choices()
    stt = get_stuff_type_choices()
    drt = get_dirt_type_choices()
    print(pdt)
    if request.method == "POST":
        form = PhotoUploadForm(pdt,
                               stt,
                               drt,
                               request.POST, request.FILES)
        if form.is_valid():
            filename1 = load_image(request, name="image1")
            filename2 = load_image(request, name="image2")
            type_product = int(form.cleaned_data['type_product'])
            type_stuff = int(form.cleaned_data['type_stuff'])
            type_dirt = int(form.cleaned_data['type_dirt'])
            photo = Photo(
                photo_before=filename1,
                photo_after=filename2,
                type_of_product=ProductType.objects.get(id=type_product),
                type_of_dirt=DirtType.objects.get(id=type_dirt),
                type_of_stuff=StuffType.objects.get(id=type_stuff),
            )
            photo.save()
            return redirect(f"/admin?u={context['username']}&p={context['password']}")
        else:
            context['errors'] = form.errors
    else:
        form = PhotoUploadForm(pdt,
                               stt,
                               drt)
        context['form'] = form
    return render(request, "pages/upoad_photo.html", context)


@front
def admin_product_create(request: WSGIRequest):
    context = {
        'menu': get_menu_context(),
        'username': request.GET.get("u"),
        'password': request.GET.get("p"),
    }
    if request.method == "POST":
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = ProductType(type=form.cleaned_data['name'])
            product.save()
            return redirect(f"/admin?u={context['username']}&p={context['password']}")
        else:
            context['errors'] = form.errors
    else:
        form = ProductCreateForm()
        context['form'] = form
    return render(request, "pages/create_product.html", context)


@front
def admin_product_view_all(request: WSGIRequest, action_type: str):
    context = {'menu': get_menu_context(),
               'username': request.GET.get("u"),
               'password': request.GET.get("p"),
               "data": list(ProductType.objects.all()),
               "action_type": action_type,
               }
    return render(request, "pages/view_products.html", context)


@front
def admin_product_edit(request: WSGIRequest, type_id: int):
    context = {'menu': get_menu_context(),
               'username': request.GET.get("u"),
               'password': request.GET.get("p"),
               }
    cur_product = ProductType.objects.get(id=type_id)
    if request.method == "POST":
        form = ProductEditForm(request.POST, instance=cur_product)
        if form.is_valid():
            form.save()
            return redirect(f"/admin/product/view/edit/?u={context['username']}&p={context['password']}")
        else:
            context['errors'] = form.errors
    else:
        form = ProductEditForm(instance=cur_product)
        context['form'] = form
    return render(request, "pages/edit_product.html", context)


@front
def admin_product_delete(request: WSGIRequest, type_id: int):
    context = {'menu': get_menu_context(),
               'username': request.GET.get("u"),
               'password': request.GET.get("p"),
               }
    product_type: ProductType = ProductType.objects.get(id=type_id)
    for i in product_type.photo_set.all():
        i: Photo
        i.delete()
    product_type.delete()
    return redirect(f"/admin/product/view/delete/?u={context['username']}&p={context['password']}")


def admin_error(request: WSGIRequest, exception):
    context = {'menu': get_menu_context()}
    return render(request, 'base/does_not_found.html', context=context, status=404)

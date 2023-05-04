"""
URL configuration for Hakanet2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler404
from django.urls import path, include, re_path
from main import views

handler404 = "main.views.admin_error"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.start_page),
    re_path("^test", views.test),
    re_path("^signup", views.signup),
    re_path("^login", views.login),
    re_path("^logout", views.logout),
    re_path("^get/user", views.get_user),
    re_path("^get/articles", views.get_all_articles),
    re_path("^get/main_page", views.get_main_page),
    re_path("^get/services", views.get_services),
    path("get/service/<int:service_id>", views.get_services),
    re_path("^image_upload", views.image_upload),
    path("admin/error/", views.admin_error, name="error"),
    re_path("^admin/photo_upload", views.admin_photo_upload, name="photo_upload"),
    re_path("^admin/product/create", views.admin_product_create, name="product_create"),
    re_path("^admin/stuff/create", views.admin_stuff_create, name="stuff_create"),
    re_path("^admin/dirt/create", views.admin_dirt_create, name="dirt_create"),
    re_path("^admin/time/create", views.admin_time_create, name="time_create"),
    path("admin/product/view/<str:action_type>/", views.admin_product_view_all, name="product_view_edit"),
    path("admin/stuff/view/<str:action_type>/", views.admin_stuff_view_all, name="stuff_view_edit"),
    path("admin/dirt/view/<str:action_type>/", views.admin_dirt_view_all, name="dirt_view_edit"),
    path("admin/time/view/<str:action_type>/", views.admin_time_view_all, name="time_view_edit"),
    path("admin/product/edit/<str:type_id>/", views.admin_product_edit, name="product_edit"),
    path("admin/stuff/edit/<str:type_id>/", views.admin_stuff_edit, name="stuff_edit"),
    path("admin/dirt/edit/<str:type_id>/", views.admin_dirt_edit, name="dirt_edit"),
    path("admin/time/edit/<str:type_id>/", views.admin_time_edit, name="time_edit"),
    path("admin/product/delete/<str:type_id>/", views.admin_product_delete, name="product_delete"),
    path("admin/stuff/delete/<str:type_id>/", views.admin_stuff_delete, name="stuff_delete"),
    path("admin/dirt/delete/<str:type_id>/", views.admin_dirt_delete, name="dirt_delete"),
    path("admin/time/delete/<str:type_id>/", views.admin_time_delete, name="time_delete"),
    re_path("^admin/photo/view", views.admin_image_view_all, name="photo_view"),
    path("admin/photo/delete/<int:photo_id>/", views.admin_image_delete, name="photo_delete"),
    re_path("^admin", views.admin_start, name="admin"),
]

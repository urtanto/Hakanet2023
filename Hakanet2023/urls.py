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
from django.contrib import admin
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.start_page),
    re_path("test", views.test),
    re_path("signup", views.signup),
    re_path("login", views.login),
    re_path("logout", views.logout),
    re_path("get/user", views.get_user),
    re_path("get/articles", views.get_all_articles),
    re_path("get/main_page", views.get_main_page),
    re_path("get/services", views.get_services),
    re_path("get/service/<int:service_id>", views.get_services),
]

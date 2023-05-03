from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import get_user_model


class User(AbstractUser):
    """
    Класс пользователя

    :param status: если честно хз :class:`django.contrib.auth.models.AbstractUser`
    """


class Review_for_company(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    comment = models.TextField()


class Dirt_level(models.Model):
    level = models.TextField()


class Product_type(models.Model):
    type = models.TextField()


class Stuff_type(models.Model):
    type = models.TextField()


class Time_type(models.Model):
    type = models.TextField()


class Service(models.Model):
    description = models.TextField()
    cost = models.FloatField()
    name = models.TextField()


class Photo(models.Model):
    photo = models.ImageField()
    type_of_product = models.ForeignKey(Product_type, models.CASCADE)
    type_of_stuff = models.ForeignKey(Stuff_type, models.CASCADE)
    type_of_time = models.ForeignKey(Time_type, models.CASCADE)
    level_of_dirt = models.ForeignKey(Dirt_level, models.CASCADE)


class Article(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    text = models.TextField()


class Comment_for_Article(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    article = models.ForeignKey(Article, models.CASCADE)
    text = models.TextField()

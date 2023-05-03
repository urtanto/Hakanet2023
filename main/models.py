from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class User(AbstractUser):
    """
    Класс пользователя

    :param status: если честно хз :class:`django.contrib.auth.models.AbstractUser`
    """
    super_user = models.BooleanField(default=False)


class ReviewForCompany(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    comment = models.TextField()


class DirtLevel(models.Model):
    level = models.TextField()


class ProductType(models.Model):
    type = models.TextField()


class StuffType(models.Model):
    type = models.TextField()


class TimeType(models.Model):
    type = models.TextField()


class Service(models.Model):
    description = models.TextField()
    cost = models.FloatField()
    name = models.TextField()


class Photo(models.Model):
    photo_before = models.TextField()
    photo_after = models.TextField()
    type_of_product = models.ForeignKey(ProductType, models.CASCADE)
    type_of_stuff = models.ForeignKey(StuffType, models.CASCADE)
    type_of_time = models.ForeignKey(TimeType, models.CASCADE)
    level_of_dirt = models.ForeignKey(DirtLevel, models.CASCADE)


class Article(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    name = models.TextField()
    text = models.TextField()


class CommentForArticle(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    article = models.ForeignKey(Article, models.CASCADE)
    text = models.TextField()


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    service = models.ForeignKey(Service, models.CASCADE)
    status = models.IntegerField()
    type_of_product = models.ForeignKey(ProductType, models.CASCADE)
    type_of_stuff = models.ForeignKey(StuffType, models.CASCADE)
    level_of_dirt = models.ForeignKey(DirtLevel, models.CASCADE)
    type_of_time = models.ForeignKey(TimeType, models.CASCADE)

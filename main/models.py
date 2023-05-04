import json

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
    """
    Comments about company
    """
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    comment = models.TextField()


class DirtType(models.Model):
    """
    Dirt levels
    """
    type = models.CharField(max_length=255)


class ProductType(models.Model):
    """
    type of product
    """
    type = models.CharField(max_length=255)


class StuffType(models.Model):
    """
    type of material
    """
    type = models.CharField(max_length=255)


class TimeType(models.Model):
    """
    Type how fast we have to do it
    """
    type = models.CharField(max_length=255)


class Service(models.Model):
    """
    Services of company
    """
    description = models.TextField()
    cost = models.FloatField()
    name = models.TextField(default="")


class Photo(models.Model):
    """
    Object for carousel with before/after
    """
    photo_before = models.TextField()
    photo_after = models.TextField()
    type_of_product = models.ForeignKey(ProductType, models.CASCADE)
    type_of_stuff = models.ForeignKey(StuffType, models.CASCADE)
    type_of_dirt = models.ForeignKey(DirtType, models.CASCADE)


class Article(models.Model):
    """
    Article in the blog
    """
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    name = models.TextField(default="")
    text = models.TextField()


class CommentForArticle(models.Model):
    """
    Comments for article
    """
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    article = models.ForeignKey(Article, models.CASCADE)
    text = models.TextField()


class Order(models.Model):
    """
    Order to do some job
    """
    user = models.ForeignKey(get_user_model(), models.CASCADE)
    service = models.ForeignKey(Service, models.CASCADE)
    extra_services = models.TextField(default="")  # Needs parse json
    status = models.IntegerField()
    type_of_product = models.ForeignKey(ProductType, models.CASCADE)
    type_of_stuff = models.ForeignKey(StuffType, models.CASCADE)
    level_of_dirt = models.ForeignKey(DirtType, models.CASCADE)
    type_of_time = models.ForeignKey(TimeType, models.CASCADE)
    taken = models.BooleanField(default=False)

    def set_extra_services(self, x: [dict, list]):
        """
        export data to db
        :param x: data like dict or list
        """
        self.extra_services = json.dumps(x)

    def get_extra_services(self):
        """
        import data from db
        :return: data like dict or list
        """
        return json.loads(self.extra_services)

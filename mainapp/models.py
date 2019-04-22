from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class ExtraCategory(models.Model):
    category_type = models.CharField(max_length=15, default="None", unique=True)

    def __str__(self):
        return self.category_type


class Extra(models.Model):
    category = models.ForeignKey(ExtraCategory, on_delete=models.CASCADE)
    extra_type = models.CharField(max_length=200)
    price_night = models.IntegerField(default=0)

    def __str__(self):
        return self.extra_type


class RoomType(models.Model):
    type = models.CharField(max_length=15)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.type


class DiscountedPacks(models.Model):
    category = models.ForeignKey(ExtraCategory, on_delete=models.CASCADE)
    pack_type = models.CharField(max_length=200)
    pack_price_night = models.IntegerField(default=0)

    def __str__(self):
        return self.extra_type



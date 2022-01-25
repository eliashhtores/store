from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel


class Color(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    man = models.BooleanField(default=True)
    woman = models.BooleanField(default=False)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to='products/', blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    colors = models.ManyToManyField(Color)
    video = models.URLField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    sales = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

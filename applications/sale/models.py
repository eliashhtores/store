from re import U
from django.db import models
from django.conf import settings
from model_utils.models import TimeStampedModel
from applications.product.models import Product, Color
from .managers import DetailManager


class Sale(TimeStampedModel):
    PAYMENT_TYPE_CHOICES = (
        ('0', 'CARD'),
        ('1', 'TRANSFER'),
        ('2', 'UPON DELIVERY'),
    )

    INVOICE_TYPE_CHOICES = (
        ('0', 'TICKET'),
        ('1', 'INVOICE'),
        ('2', 'OTHER'),
    )

    STATE_CHOICES = (
        ('0', 'In process'),
        ('1', 'Sent'),
        ('2', 'In store'),
        ('3', 'Delivered'),
    )

    date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    payment_type = models.CharField(max_length=2, choices=PAYMENT_TYPE_CHOICES)
    invoice_type = models.CharField(max_length=2, choices=INVOICE_TYPE_CHOICES)
    state = models.CharField(
        max_length=2, choices=STATE_CHOICES, default=STATE_CHOICES[0][0])
    canceled = models.BooleanField(default=False)
    address = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return f'Nº {str(self.id)} - {str(self.date)}'


class Detail(TimeStampedModel):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(
        default=1, null=True, blank=True)
    canceled = models.BooleanField(default=False)

    objects = DetailManager()

    def __str__(self):
        return f'{str(self.id)} - {str(self.product.name)}'

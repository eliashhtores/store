from django.db import models


class DetailManager(models.Manager):

    def get_sale_detail(self, sale):
        return self.filter(sale=sale).order_by('product__name')

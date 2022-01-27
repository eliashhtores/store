from django.db import models


class DetailManager(models.Manager):

    def get_sale_detail(self, sale_id):
        return self.filter(sale__id=sale_id).order_by('product__name')

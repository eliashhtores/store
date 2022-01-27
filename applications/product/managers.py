from django.db import models


class ProductManager(models.Manager):
    def products_by_user(self, created_by_id):
        return self.filter(created_by_id=created_by_id)

    def get_product_stock(self):
        return self.filter(stock__gt=0).order_by('sales')

    def products_by_gender(self, gender):
        woman = True
        man = True
        if gender == 'm':
            woman = False
            return self.filter(woman=woman, man=man)
        if gender == 'w':
            man = False
            return self.filter(woman=woman, man=man)
        return self.filter(woman=woman, man=man)

    def filter_products(self, **kwargs):
        return self.filter(woman=kwargs['woman'], man=kwargs['man'], name__icontains=kwargs['name'])

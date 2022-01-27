from django.db import models


class ProductManager(models.Manager):
    def products_by_user(self, created_by_id):
        return self.filter(created_by_id=created_by_id)

    def get_product_stock(self):
        return self.filter(stock__gt=0).order_by('sales')

    def products_by_gender(self, gender):
        if gender == 'm':
            return self.filter(gender=gender)
        if gender == 'w':
            return self.filter(gender=gender)
            return self.filter(gender=gender)

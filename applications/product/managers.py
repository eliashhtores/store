from django.db import models


class ProductManager(models.Manager):
    def products_by_user(self, created_by_id):
        return self.filter(created_by_id=created_by_id)

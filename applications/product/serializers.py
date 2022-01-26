from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')
        # fields = ('name', 'description', 'stock')
        # extra_kwargs = {
        #     'product': {'view_name': 'product_app_api:api_detail', 'lookup_field': 'pk'}
        # }

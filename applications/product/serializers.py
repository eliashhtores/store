from rest_framework import serializers, pagination
from .models import Product, Color


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):

    colors = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('__all__')
        # fields = ('name', 'description', 'stock')
        # extra_kwargs = {
        #     'product': {'view_name': 'product_app_api:api_detail', 'lookup_field': 'pk'}
        # }


class ProductPaginatorSerializer(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


class ProductViewSetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('__all__')

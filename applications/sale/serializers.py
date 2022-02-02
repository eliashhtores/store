from rest_framework import serializers
from applications.product.serializers import ProductSerializer
from .models import Sale, Detail


class DetailSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Detail
        fields = ('__all__')


class SaleSerializer(serializers.ModelSerializer):

    products = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = ('__all__')

    def get_products(self, obj):
        query = Detail.objects.get_sale_detail(obj)
        products = DetailSerializer(query, many=True).data
        return products


class ProcessDetailSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    quantity = serializers.IntegerField()
    color = serializers.IntegerField()


class ProcessSaleSerializer(serializers.Serializer):

    invoice_type = serializers.CharField()
    payment_type = serializers.CharField()
    address = serializers.CharField()
    products = ProcessDetailSerializer(many=True)

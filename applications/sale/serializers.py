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
        query = Detail.objects.get_sale_detail(obj.id)
        products = DetailSerializer(query, many=True).data
        return products


class ProcessDetailSerializer(serializers.Serializer):

    sale = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ProcessSaleSerializer(serializers.Serializer):

    invoice_type = serializers.CharField()
    payment_type = serializers.CharField()
    address = serializers.CharField()
    products = ProcessDetailSerializer(many=True)

    # def process_sale(self, data):
    #     sale = Sale.objects.create(**data)
    #     for product in data['products']:
    #         Detail.objects.create(
    #             sale=sale,
    #             product=Product.objects.get(id=product['id']),
    #             quantity=product['quantity'],
    #         )
    #     return sale
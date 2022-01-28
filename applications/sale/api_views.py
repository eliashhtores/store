from django.utils import timezone
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Sale, Detail
from .serializers import SaleSerializer, ProcessSaleSerializer


class SaleListAPIView(ListAPIView):
    serializer_class = SaleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Sale.objects.all()


class CreateSaleAPIView(CreateAPIView):
    serializer_class = ProcessSaleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request):
        serializer = ProcessSaleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice_type = serializer.validated_data['invoice_type']
        payment_type = serializer.validated_data['payment_type']
        address = serializer.validated_data['address']
        sale = Sale.objects.create(
            date=timezone.now(),
            amount=0,
            quantity=0,
            invoice_type=invoice_type,
            payment_type=payment_type,
            address=address,
            user=request.user
        )
        products = serializer.validated_data['products']
        details = []

        for product in products:
            detail = Detail(
                sale=sale,
                product_id=product['id'],
                quantity=product['quantity'],
            )
            details.append(detail)

        sale.amount = sum(
            [detail.product.price * detail.quantity for detail in details])
        sale.quantity = sum([detail.quantity for detail in details])
        sale.save()

        Detail.objects.bulk_create(details)

        return Response(SaleSerializer(sale).data, status=201)

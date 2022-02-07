from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from applications.product.models import Color
from .models import Sale, Detail
from .serializers import SaleSerializer, ProcessSaleSerializer


class SaleListAPIView(ListAPIView):
    serializer_class = SaleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Sale.objects.all()


class SaleViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    queryset = Sale.objects.all().order_by('-id')

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = Sale.objects.all().order_by('-id')
        serializer = SaleSerializer(queryset, many=True)
        return Response(serializer.data)

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
            color = Color.objects.get(id=product['color'])
            detail = Detail(
                sale=sale,
                product_id=product['id'],
                quantity=product['quantity'],
                color=color
            )
            details.append(detail)

        sale.amount = sum(
            [detail.product.price * detail.quantity for detail in details])
        sale.quantity = sum([detail.quantity for detail in details])
        sale.save()

        Detail.objects.bulk_create(details)

        return Response(SaleSerializer(sale).data, status=201)

    def retrieve(self, request, pk=None):
        sale = get_object_or_404(Sale.objects.all(), pk=pk)
        serializer = SaleSerializer(sale)
        return Response(serializer.data)

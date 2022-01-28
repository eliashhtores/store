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

    def create(self, request, *args, **kwargs):
        serializer = ProcessSaleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice_type = serializer.validated_data['invoice_type']
        payment_type = serializer.validated_data['payment_type']
        address = serializer.validated_data['address']

        return Response({'test': 'ok'})

        # data = request.data
        # sale = Sale.objects.create(
        #     invoice_type=data['invoice_type'],
        #     payment_type=data['payment_type'],
        #     address=data['address'],
        # )
        # for product in data['products']:
        #     Detail.objects.create(
        #         sale=sale,
        #         product_id=product['id'],
        #         quantity=product['quantity'],
        #     )
        # return super().create(request, *args, **kwargs)

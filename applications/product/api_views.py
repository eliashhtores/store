from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Product, Color
from .serializers import ProductSerializer, ColorSerializer


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorSerializer
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Color.objects.all()


class ProductListByUserAPIView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.products_by_user(created_by_id=self.request.user)


class ProductStockAPIView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Product.objects.get_product_stock()


class ProductByGenderAPIView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return Product.objects.products_by_gender(self.kwargs['gender']).order_by('id')


class ProductFilterAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter_products(
            man=self.request.query_params.get('man', None),
            woman=self.request.query_params.get('woman', None),
            name=self.request.query_params.get('name', None)
        )

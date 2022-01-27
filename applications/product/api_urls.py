from django.urls import path
from . import api_views


app_name = "product_app_api"

urlpatterns = [
    path('api/v1/product/by_user',
         api_views.ProductListByUserAPIView.as_view(), name='by_user'),
    path('api/v1/product/stock',
         api_views.ProductStockAPIView.as_view(), name='stock'),
    path('api/v1/product/by-gender/<gender>',
         api_views.ProductByGenderAPIView.as_view(), name='by_gender'),
    path('api/v1/product/filter',
         api_views.ProductFilterAPIView.as_view(), name='filter'),
]

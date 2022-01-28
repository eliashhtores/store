from django.urls import path
from . import api_views


app_name = "sale_app_api"

urlpatterns = [
    path('api/v1/sale/list',
         api_views.SaleListAPIView.as_view(), name='sale-list'),
    path('api/v1/sale/create',
         api_views.CreateSaleAPIView.as_view(), name='sale-create'),
]

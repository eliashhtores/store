from django.urls import path
from . import api_views


app_name = "product_app_api"

urlpatterns = [
    path('api/v1/product/by_user',
         api_views.ProductListByUserAPIView.as_view(), name='by_user'),
]

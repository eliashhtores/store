from django.urls import path
from . import api_views


app_name = "user_app_api"

urlpatterns = [
    path('api/v1/user/login', api_views.GoogleLoginView.as_view(), name='login'),
]

from django.urls import path
from . import views


app_name = "user_app"

urlpatterns = [
    path('user/login', views.LoginUserView.as_view(), name='login'),
]

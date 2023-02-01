from django.urls import path
from . import views

urlpatterns = [
    # 用户注册
    path("register/", views.RegisterView.as_view(), name='register'),
]

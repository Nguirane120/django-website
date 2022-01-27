from django.urls import path, re_path
from . import views
# app_name = account

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("custumer/", views.custumer, name="custumer"),
]
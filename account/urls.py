from django.urls import path, re_path
from . import views
# app_name = account

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    # path("products/", views.custumer, name="custumer"),
    path("custumer/<str:pk>/", views.custumer, name="customer"),
    path('create-order/<str:pk>/', views.createOrder, name="createOrder"),
    path('update-order/<str:pk>/', views.updateeOrder, name="updateOrder"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="deleteOrder"),
]
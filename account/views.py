from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    custumers = Custumer.objects.all()
    total_customers = Custumer.objects.count()
    orders = Order.objects.all()
    total_orders = Order.objects.count()
    total_delivred = Order.objects.filter(status='Delivred').count()
    total_pending = Order.objects.filter(status='Pending').count()
    context = {"custumers":custumers, "orders":orders,
                "total_customers":total_customers,
                "total_orders":total_orders,
                "total_delivred":total_delivred,
                "total_pending":total_pending }

    return render(request, 'account/dashboard.html', context)

def products(request):
     products = Product.objects.all()
     return render(request, 'account/products.html', {"products":products})

def custumer(request):
    return render(request, 'account/custumer.html', {})
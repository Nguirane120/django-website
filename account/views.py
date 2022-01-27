from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'account/dashboard.html', {})

def products(request):
    return render(request, 'account/products.html', {})

def custumer(request):
    return render(request, 'account/custumer.html', {})
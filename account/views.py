from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .searchs import SearchFilter

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

def custumer(request, pk):
    custumer = Custumer.objects.get(id=pk)
    orders = custumer.order_set.all()
    orders_count = orders.count()
    search = SearchFilter(request.GET, queryset=orders)
    orders = search.qs
    context = {"custumer":custumer, "orders":orders, "orders_count":orders_count, "search":search}
    return render(request, 'account/custumer.html', context)

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Custumer, Order, fields=('product', 'status'), extra=10)
    customer = Custumer.objects.get(id=pk)
    # form = OrderForm(initial={"customer":customer})
    form_set = OrderFormSet(queryset = Order.objects.none(), instance=customer)
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        form_set = OrderFormSet(request.POST, instance=customer)

        if form_set.is_valid():
            form_set.save()
            return redirect('/')
    context= {"form_set":form_set}
    return render(request, "account/order_form.html", context)

def updateeOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {"form":form}
    return render(request, "account/order_form.html", context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {"order":order}
    return render(request, 'account/delete_order.html', context)
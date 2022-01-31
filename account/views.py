from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CreateUserform
from .searchs import SearchFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        sign = CreateUserform()
        if request.method == 'POST':
            sign = CreateUserform(request.POST)
            if sign.is_valid():
                sign.save()
                username = sign.cleaned_data.get('username')
                
                messages.success(request, "Account was created for " + username)
        context = {"sign":sign}
        return render(request, 'account/register.html', context)
        


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or passwor is incoorect')

        context = {}
        return render(request, 'account/login.html', context)
            

def logOutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def products(request):
     products = Product.objects.all()
     return render(request, 'account/products.html', {"products":products})

@login_required(login_url='login')
def custumer(request, pk):
    custumer = Custumer.objects.get(id=pk)
    orders = custumer.order_set.all()
    orders_count = orders.count()
    search = SearchFilter(request.GET, queryset=orders)
    orders = search.qs
    context = {"custumer":custumer, "orders":orders, "orders_count":orders_count, "search":search}
    return render(request, 'account/custumer.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {"order":order}
    return render(request, 'account/delete_order.html', context)



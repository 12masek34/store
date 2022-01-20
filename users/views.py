from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, logout, login
from .models import *
from django.forms import modelformset_factory
from .forms import *
from .queries import *


def index(request):
    auth = user_is_auth(request)
    if auth:
        user = request.user
    else:
        user = ''
    categories = Category.objects.all()
    products = Product.objects.all()
    if request.GET.get('question'):
        query = request.GET.get('question')
        products = Product.objects.filter(title__icontains=query)
        print(query)
        print( products)

    context = {
        'auth': auth,
        'user': user,
        'categories': categories,
        'products': products,
    }
    return render(request, 'users/index.html', context)


def login_form(request):
    auth = user_is_auth(request)
    if request.method == 'POST':
        form = AuthUserForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        form = AuthUserForm()
    context = {
        'form': form,
        'auth': auth,
    }
    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password2')
        form.save()
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('index')
    context = {
        'form': form
    }
    return render(request, 'users/reg.html', context)


def category(request, pk=None):
    products = Product.objects.filter(category=pk)
    categories = Category.objects.all()
    user = request.user
    auth = user_is_auth(request)
    context = {
        'products': products,
        'categories': categories,
        'user': user,
        'auth': auth,
    }
    return render(request, 'users/category.html', context)


def add_product(request):
    user = request.user
    auth = user_is_auth(request)
    form = AddProduct(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'auth': auth,
        'form': form,
        'user': user,
    }
    return render(request, 'users/add_product.html', context)


def product(request, pk=None):
    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    user = request.user
    auth = user_is_auth(request)
    context = {
        'product': product,
        'categories': categories,
        'user': user,
        'auth': auth,
    }
    return render(request, 'users/product.html', context)
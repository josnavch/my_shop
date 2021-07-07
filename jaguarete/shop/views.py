from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserForm
from .models import Categorias, Productos
 
 
# Create your views here.
def index(request):
    return render(request, 'base.html')
 
def product_list(request, category_id=None):
    category = None
    categories = Categorias.objects.all()
    products = Productos.objects.all()


    if category_id:
        category = get_object_or_404(Categorias, id_cat=category_id)
        products = products.filter(categoria=category)
    return render(request, 'list.html', {
            'category': category, 
            'categories': categories, 
            'productos': products
            })
 
def product_detail(request, id, sku):
    product = get_object_or_404(Productos, id=id, sku=sku)
    return render(request, 'detail.html', {'product': product})

def acerca(request):
   return render(request, 'acerca.html')

def contacto(request):
   return render(request, 'contacto.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('shop:base')
        else:
            messages.info(request, 'Try again! username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def logout_page(request):
    logout(request)
    return redirect('shop:base')

@login_required(login_url='shop:login')

def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:login')
    context = {'form': form}
    return render(request, 'register.html', context)
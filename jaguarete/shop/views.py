from django.shortcuts import render, get_object_or_404, redirect
 
from .models import Categorias, Productos
 
 
# Create your views here.
 
 
 
def product_list(request, category_id=None):
    category = None
    categories = Categorias.objects.all()
    products = Productos.objects.all()
    if category_id:
        category = get_object_or_404(Categorias, id_cat=category_id)
        products = products.filter(categoria=category)
    return render(request, 'shop/templates/list.html',
                  {'categoria': category, 'categories': categories,
                   'productos': products})

def product_detail(request, id, sku):
    product = get_object_or_404(Productos, id=id, sku=sku)
    return render(request, 'shop/templates/detail.html', {'product': product})
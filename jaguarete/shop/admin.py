from django.contrib import admin
 
from .models import Categorias, Productos
 
 
# Register your models here.
 
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'id_cat']
    prepopulated_fields = {'id_cat': ('descripcion',)}
 
 
admin.site.register(Categorias, CategoriasAdmin)
 
 
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'sku', 'precio', 'cantidad']
    list_filter = ['titulo', 'precio']
    list_editable = ['precio', 'cantidad']
    prepopulated_fields = {'sku': ('titulo',)}
 
 
admin.site.register(Productos, ProductosAdmin)
 

from django.urls import path
 
from . import views
 
app_name = 'shop'

urlpatterns = [
     path ('product_list/', views.product_list, name='product_list'),
     path ('<slug:id_cat>', views.product_list, name='product_list_by_category'),
     path ('<int:id>/<slug:sku>/', views.product_detail, name='product_detail'), 
]
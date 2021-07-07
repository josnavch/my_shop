from django.urls import path
 
from . import views
 
app_name = 'shop'

urlpatterns = [
     path ('', views.index, name='base'),
     path ('login', views.login_page, name='login'),
     path ('logout', views.logout_page, name='logout'),
     path ('register', views.register_page, name='register'),
     path ('contacto', views.contacto, name='contacto'), 
     path ('acerca', views.acerca, name='acerca'), 
     
     path ('product_list', views.product_list, name='product_list'),
     path ('<slug:category_id>', views.product_list, name='product_list_by_category'),
     path ('<int:id>/<slug:sku>/', views.product_detail, name='product_detail'),
     
]
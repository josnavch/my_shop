from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


 
 
# Create your models here.
 
class Categorias(models.Model):
    descripcion = models.CharField(max_length=200, db_index=True)
    id_cat = models.SlugField(max_length=200, db_index=True, unique=True)
 
    class Meta:
        ordering = ('descripcion',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
 
    def __str__(self):
        return self.descripcion
    
    def save(self, *args, **kwargs):
        if not self.id_cat:
            self.id_cat = slugify(self.descripcion)
        super(Categorias, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.id_cat])
 
 
class Productos(models.Model):
    categoria = models.ForeignKey(Categorias, related_name='productos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200, db_index=True)
    sku = models.SlugField(max_length=200, db_index=True)
    imagen = models.ImageField(upload_to='shop/static/media/productos', blank=True)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
 
    class Meta:
        ordering = ('titulo',)
        index_together = (('id', 'sku'),)
 
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = slugify(self.titulo)
        super(Productos, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.sku])

class Carrito(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Productos)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


  
  
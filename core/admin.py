from django.contrib import admin

# Register your models here.

from .models import Articulo

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'ubicacion', 'fecha_subida', 'fecha_actualizacion')
    search_fields = ('nombre', 'descripcion', 'ubicacion')

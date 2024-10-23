from django.contrib import admin
from .models import Articulo, Comentario  

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'ubicacion', 'fecha_subida', 'fecha_actualizacion')
    search_fields = ('nombre', 'descripcion', 'ubicacion')

@admin.register(Comentario)  
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'articulo', 'texto', 'fecha_creacion')  
    search_fields = ('usuario__username', 'articulo__nombre')  
    list_filter = ('articulo', 'fecha_creacion')  
    ordering = ('-fecha_creacion',)  

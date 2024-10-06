from django.contrib import admin
from .models import Articulo, Comentario  # Asegúrate de importar el modelo Comentario

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'ubicacion', 'fecha_subida', 'fecha_actualizacion')
    search_fields = ('nombre', 'descripcion', 'ubicacion')

@admin.register(Comentario)  # Registra el modelo Comentario
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'articulo', 'texto', 'fecha_creacion')  # Ajusta estos campos según tu modelo
    search_fields = ('usuario__username', 'articulo__nombre')  # Campos que deseas poder buscar
    list_filter = ('articulo', 'fecha_creacion')  # Filtros disponibles en el admin
    ordering = ('-fecha_creacion',)  # Ordenar por fecha de creación descendente

from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
from .models import Articulo
# Create your views here.
def inicio(request):
    return render(request,'core/index.html');



class ArticuloListView(ListView):
    model = Articulo
    # template_name = 'core/articulo_list.html'
    template_name = 'core/index.html'
    context_object_name = 'articulos'
    paginate_by = 4
    ordering = ['-fecha_subida']

from django.views.generic.detail import DetailView

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'core/articulo_detail.html'
    context_object_name = 'articulo'

class ArticuloViewAll(ListView):
    model = Articulo
    template_name = 'core/articulos_listado.html'
    context_object_name = 'articulos'
    paginate_by = 4    
    ordering = ['-fecha_subida']


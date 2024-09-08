from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
from .models import Articulo
# Create your views here.
def inicio(request):
    return render(request,'core/index.html');



class ArticuloListView(ListView):
    model = Articulo
    template_name = 'core/articulo_list.html'
    context_object_name = 'articulos'
    paginate_by = 12

from django.views.generic.detail import DetailView

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'core/articulo_detail.html'
    context_object_name = 'articulo'


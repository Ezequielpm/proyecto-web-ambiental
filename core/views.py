from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
from .models import Articulo
from django.views.generic.edit import CreateView
from .forms import ArticuloForm
from django.urls import reverse_lazy
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


class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'core/articulo_form.html'
    success_url = reverse_lazy('articulos-view-all')  # Redirigir a una página de éxito

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asignar el usuario actual al artículo
        return super().form_valid(form)
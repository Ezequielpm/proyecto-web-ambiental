from django.shortcuts import render,HttpResponse
from django.views.generic import ListView
from .models import Articulo
from django.views.generic.edit import CreateView
from .forms import ArticuloForm
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.utils.timesince import timesince
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtener el artículo actual
        articulo = self.object
        # Obtener artículos relacionados (puedes ajustar la lógica según tus necesidades)
        related_articulos = Articulo.objects.exclude(pk=articulo.pk).order_by('?')[:9]  # 3 artículos aleatorios
        context['related_articulos'] = related_articulos
        for articulo in context['related_articulos']:
            articulo.tiempo_transcurrido = timesince(articulo.fecha_subida)  # Tiempo desde la subida
        return context

class ArticuloViewAll(ListView):
    model = Articulo
    template_name = 'core/articulos_listado.html'
    context_object_name = 'articulos'
    paginate_by = 16    
    ordering = ['-fecha_subida']


class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'core/articulo_form.html'
    success_url = reverse_lazy('articulos-view-all')  # Redirigir a una página de éxito

    def form_valid(self, form):
        form.instance.usuario = self.request.user  # Asignar el usuario actual al artículo
        return super().form_valid(form)
from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Articulo, Comentario
from django.views.generic.edit import CreateView
from .forms import ArticuloForm
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.utils.timesince import timesince
from django.contrib.auth.decorators import login_required

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

# from django.views.generic.detail import DetailView

from django.views.generic import DetailView
from .forms import ComentarioForm  

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'core/articulo_detail.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articulo = self.object
        related_articulos = Articulo.objects.exclude(pk=articulo.pk).order_by('?')[:9]
        
       
        comentarios = Comentario.objects.filter(articulo=articulo).order_by('fecha_creacion')
        
        context['related_articulos'] = related_articulos
        context['comentarios'] = comentarios
        context['form'] = ComentarioForm()  
        for articulo in context['related_articulos']:
            articulo.tiempo_transcurrido = timesince(articulo.fecha_subida)

        return context

    def post(self, request, *args, **kwargs):
        articulo = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.articulo = articulo
            comentario.usuario = request.user  # Asignar el usuario actual al comentario
            comentario.save()
            return redirect('articulo-detail', pk=articulo.pk)  # Redirigir a la misma página del artículo

        # Si el formulario no es válido, se muestra de nuevo el formulario
        return self.get(request, *args, **kwargs)


@login_required
def eliminar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)

    # Asegurarte de que el usuario que intenta eliminar el comentario sea el que lo creó
    if comentario.usuario == request.user:
        comentario.delete()
    
    # Redirige a la misma página del artículo después de eliminar el comentario
    return redirect('articulo-detail', pk=comentario.articulo.pk)


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
    
def nosotros(request):
    return render(request,'core/about.html')    
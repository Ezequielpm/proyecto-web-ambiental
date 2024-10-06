from django.shortcuts import render,HttpResponse, redirect, get_object_or_404
from django.views.generic import ListView,View
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


from .models import Mensaje
from .forms import MessageForm

class MessageThreadView(View):
    def get(self, request, articulo_id):
        articulo = get_object_or_404(Articulo, pk=articulo_id)
        messages = Mensaje.objects.filter(articulo=articulo)
        form = MessageForm()  # Asegúrate de inicializar el formulario
        return render(request, 'core/message_thread.html', {
            'articulo': articulo,
            'messages': messages,
            'form': form,  # Pasar el formulario al contexto
        })



from .models import Mensaje  # Asegúrate de que el modelo Mensaje esté importado
from .forms import MessageForm # Asegúrate de que el formulario Mensaje esté importado

def send_message_view(request, articulo_id):
    # Obtén el artículo antes de manejar el formulario
    articulo = get_object_or_404(Articulo, pk=articulo_id)  # Obtén el artículo aquí

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.articulo_id = articulo_id  # Asignar el artículo relacionado
            mensaje.sender = request.user  # Asignar el usuario actual
            mensaje.receiver = articulo.usuario  # Asignar el dueño del artículo como receptor
            mensaje.save()
            return redirect('message_thread', articulo_id=articulo_id)
        else:
            # Si el formulario no es válido, se muestra nuevamente con errores
            messages = Mensaje.objects.filter(articulo=articulo)  # Obtén los mensajes para este artículo
            return render(request, 'core/message_thread.html', {
                'articulo': articulo,
                'messages': messages,
                'form': form,  # Pasa el formulario con errores a la plantilla
            })

    return HttpResponse('Error al enviar el mensaje', status=400)



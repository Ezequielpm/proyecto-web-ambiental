# from . import views
# from django.urls import path
# urlpatterns = [
#     path('',views.inicio,name="inicio"),
# ]

from django.urls import path
from .views import ArticuloListView,ArticuloDetailView,ArticuloViewAll
from .views import ArticuloCreateView,nosotros,eliminar_comentario,MessageThreadView,send_message_view

urlpatterns = [
    path('', ArticuloListView.as_view(), name='articulo-list'),
    path('articulo/<int:pk>/', ArticuloDetailView.as_view(), name='articulo-detail'),
    path('articulosdisponibles',ArticuloViewAll.as_view(),name="articulos-view-all"),
    path('subir-articulo/', ArticuloCreateView.as_view(), name='upload-articulo'),
    path('nosotros/',nosotros , name='nosotros'),
    path('comentario/eliminar/<int:comentario_id>/', eliminar_comentario, name='eliminar-comentario'),
    path('articulo/<int:articulo_id>/messages/', MessageThreadView.as_view(), name='message_thread'),
    path('articulo/<int:articulo_id>/send_message/', send_message_view, name='send_message'), 
]


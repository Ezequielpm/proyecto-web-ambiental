# from . import views
# from django.urls import path
# urlpatterns = [
#     path('',views.inicio,name="inicio"),
# ]

from django.urls import path
from .views import ArticuloListView,ArticuloDetailView,ArticuloViewAll
from .views import ArticuloCreateView

urlpatterns = [
    path('', ArticuloListView.as_view(), name='articulo-list'),
    path('articulo/<int:pk>/', ArticuloDetailView.as_view(), name='articulo-detail'),
    path('articulosdisponibles',ArticuloViewAll.as_view(),name="articulos-view-all"),
    path('subir-articulo/', ArticuloCreateView.as_view(), name='upload-articulo'),
]


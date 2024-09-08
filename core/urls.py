# from . import views
# from django.urls import path
# urlpatterns = [
#     path('',views.inicio,name="inicio"),
# ]

from django.urls import path
from .views import ArticuloListView,ArticuloDetailView

urlpatterns = [
    path('', ArticuloListView.as_view(), name='articulo-list'),
    path('articulo/<int:pk>/', ArticuloDetailView.as_view(), name='articulo-detail'),
]


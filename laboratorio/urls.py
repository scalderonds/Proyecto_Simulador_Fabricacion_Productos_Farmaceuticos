from django.urls import path
from . import views

urlpatterns = [
    path("", views.insertar, name="insertar"),
    path("mostrar/", views.mostrar, name="mostrar"),
    path("insertar/", views.insertar, name="insertar"),
    path('editar/<int:pk>', views.editar, name='editar'),
    path("eliminar/<int:pk>", views.eliminar, name="eliminar"),    
]

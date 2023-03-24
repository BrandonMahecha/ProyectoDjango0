from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path("", views.home,name="home"),
    path('agregar/',views.agregar,name="agregar"),
    path("eliminar/<int:tarea_id>/",views.eliminar,name="eliminar"),
    path("editar/<int:tarea_id>/",views.editar,name="editar"),
    
]

# aqui debe agregar lo siguientes path (urls),de cada HTML que se van creando en la app todo:
#     editar, eliminar, agregar
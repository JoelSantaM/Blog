from django.urls import path
from .views import listar_productos, listar_usuarios, agregar_producto, agregar_usuario

urlpatterns = [
    path('usuarios/', listar_usuarios, name='listar_usuarios'),
    path('productos/', listar_productos, name='listar_productos'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('agregar_usuario/', agregar_usuario, name='agregar_usuario'),
]
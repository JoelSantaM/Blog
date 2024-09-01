from django.urls import path
from .views import listar_productos, detalle_publicacion, agregar_producto, editar_producto

urlpatterns = [
    path('productos/', listar_productos, name='listar_producto'),
    path('productos/<int:pk>/editar/', editar_producto, name='editar_producto'),
    path('productos/<int:pk>/',detalle_publicacion, name='detalle_publicacion'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    ]
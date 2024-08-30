from django.shortcuts import render, redirect
from .models import Usuario, Producto
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ProductoModelForm, UsuarioModelForm
# Create your views here.

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,'listar_usuarios.html',{ 'usuarios': usuarios })

def listar_productos(request):
    fecha_publicacion = request.GET.get('fecha_publicacion')
    categoria = request.GET.get('categoria')
    query = request.GET.get('q')
    productos_list = Producto.objects.all()
    
    if fecha_publicacion:
        productos_list = productos_list.filter(fecha_publicacion=fecha_publicacion)
    
    if categoria:
        productos_list = productos_list.filter(categoria=categoria)

    if query:
        productos_list = productos_list.filter(Q(titulo__icontains=query)| Q(contenido__icontains=query))

    paginator = Paginator(productos_list,10)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    
    return render(request, 'listar_productos.html', { 'productos': productos })

def inicio(request):
    return render(request, 'inicio.html')


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    
    else:
        form = ProductoModelForm()
        return render(request, 'agregar_producto.html', { 'form' : form })


def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')

    else:
        form = UsuarioModelForm()
    return render(request, 'agregar_usuarios.html', { 'form': form })


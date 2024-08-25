from django.shortcuts import render, redirect
from .models import Usuario, Producto
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ProductoModelForm, UsuarioModelForm
# Create your views here.

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request,'listar_usuarios.html',{'usuarios': usuarios})

def listar_productos(request):
    query = request.GET.get('q')
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list,5)
    page_number = request.GET.get('page')
    productos = paginator.get_page('page_number')

    if query:
        productos_list = productos_list.filter(Q(nombre__icontains=query)| Q(descripcion__icontains=query))
    
    return render(request, 'listar_productos.html', {'productos': productos})

def inicio(request):
    return render(request, 'inicio.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    
    else:
        form = ProductoModelForm
        return render(request, 'agregar_prodcuto.html',{'form' : form})
    
def agregar_usuario(requets):
    if requets.method == 'POST':
        form = UsuarioModelForm(requets.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')

    else:
        form = UsuarioModelForm()
    return render(requets, 'agregar_usuarios.html', { 'form': form })

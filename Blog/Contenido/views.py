from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ProductoModelForm

# Create your views here.

def listar_productos(request):
    query = request.GET.get('q')
    categoria = request.GET.get('categoria')

    publicaciones = Producto.objects.all()

    if query:
        publicaciones = publicaciones.filter(Q(titulo__icontains=query) | Q(contenido__icontains=query))

    if categoria:
        publicaciones = publicaciones.filter(categoria__icontains=categoria)
    
    paginator = Paginator(publicaciones, 10)
    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)
    
    return render(request, 'listar_producto.html', {'productos': productos})

def inicio(request):
    return render(request, 'inicio.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')
        
        else:
            return render(request, 'agregar_producto.html', { 'form': form })
    
    else:
        form = ProductoModelForm()
        return render(request, 'agregar_producto.html', { 'form' : form })

def detalle_publicacion(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle_publicacion.html', {'producto': producto})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        form = ProductoModelForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_publicacion', pk=producto.pk)
        
    else:
        form = ProductoModelForm(instance=producto)

    return render(request, 'editar_producto.html', {'form':form, 'producto': producto})





































































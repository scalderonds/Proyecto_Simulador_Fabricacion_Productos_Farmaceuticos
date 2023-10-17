from django.shortcuts import render, redirect
from .models import Laboratorio



def mostrar(request):
    laboratorios = Laboratorio.objects.all().order_by('id')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'laboratorios': laboratorios,
        'num_visits': num_visits,
    }

    return render(request, 'mostrar.html', context)


def insertar(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']

        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('mostrar')
    else:
        return render(request, 'insertar.html')


def editar(request, pk):
    laboratorio = Laboratorio.objects.get(pk=pk)

    if request.method == "POST":
        laboratorio.nombre = request.POST['nombre']
        laboratorio.ciudad = request.POST['ciudad']
        laboratorio.pais = request.POST['pais']
        laboratorio.save()
        return redirect('mostrar')

    context = {'laboratorio': laboratorio}
    return render(request, 'editar.html', context)

def eliminar(request, pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('mostrar')
    context = {'laboratorio': laboratorio}
    return render(request, 'eliminar.html', context)

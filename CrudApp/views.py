from django.shortcuts import render, redirect

from .models import ProyectoModels
from .forms import ProyectoForms


# Create your views here.

def index(request):
    return render(request, 'index.html', {})


def listado_proyecto(request):

    listado_proyecto = ProyectoModels.objects.all()

    data = {
        'lista_proyecto': listado_proyecto
    }

    return render(request, 'listado_proyecto.html', data)


def agregar_proyecto(request):

    formulario = ProyectoForms()

    if request.method == 'POST':
        formulario = ProyectoForms(request.POST)

        if formulario.is_valid():
            formulario.save()
            print("ok")

            return redirect('listado_proyecto')

    data = {
        'titulo': 'Agregar Proyecto',
        'formulario': formulario
    }

    return render(request, 'agregar_proyecto.html', data)


def eliminar_proyecto(request, id):

    proyecto = ProyectoModels.objects.get(id=id)

    proyecto.delete()

    return redirect('listado_proyecto')


def modificar_proyecto(request, id):

    proyecto = ProyectoModels.objects.get(id=id)

    formulario = ProyectoForms(instance=proyecto)

    if request.method == 'POST':

        formulario = ProyectoForms(
            request.POST,
            instance=proyecto
        )

        if formulario.is_valid():
            formulario.save()

            return redirect('listado_proyecto')

    data = {
        'titulo': 'Modificar Proyecto',
        'formulario': formulario
    }

    return render(
        request,
        'agregar_proyecto.html',
        data
    )

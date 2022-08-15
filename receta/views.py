from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Receta

# Create your views here.


def receta(request):
    receta = Receta.objects.all()
    context = {
        "receta": receta[::-1],
        "update_from": None
    }
    return render(request, 'receta.html', context)


def insert(request):
    try:
        receta_titulo = request.POST['titulo']
        receta_descripcion = request.POST['descripcion']
        receta_fecha = request.POST['fecha']
        if receta_titulo == "" or receta_descripcion == "" or receta_fecha == "":
            raise ValueError("El texto no puede estar vacio.")
        receta = Receta(titulo=receta_titulo, descripcion=receta_descripcion, fecha=receta_fecha)
        receta.save()
        return redirect('/receta/')
    except ValueError as err:
        print(err)
        return redirect('/receta/')


def update(request):
    receta_id = request.POST["id"]
    receta_titulo = request.POST['titulo']
    receta_descripcion = request.POST['descripcion']
    receta_fecha = request.POST['fecha']  
    receta = Receta.objects.get(pk=receta_id)
    receta.titulo = receta_titulo
    receta.descripcion = receta_descripcion
    receta.fecha = receta_fecha
    receta.save()
    return redirect('/receta/')


def update_from(request, receta_id):
    receta = Receta.objects.all()
    receta_only = Receta.objects.get(pk=receta_id)
    print(receta_only)
    context = {
        "receta": receta[::-1],
        "update": receta_only
    }
    return render(request, 'receta.html', context)


def delete_receta(request, receta_id):
    receta = Receta.objects.filter(id=receta_id)
    receta.delete()
    return redirect('/receta/')

from django.shortcuts import render, redirect
from .models import Excursion

# Create your views here.

def home(request):
    excursionesListados = Excursion.objects.all()
    return render(request, "gestionExcursion.html",{"excursiones": excursionesListados} )

def registrarExcursion(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    curso = request.POST['txtCurso']
    calumnos = request.POST['numCalumnos']
    destino = request.POST['txtDestino']
    fecha = request.POST['txtFecha']

    excursion = Excursion.objects.create(codigo=codigo, nombre=nombre, curso=curso, calumnos=calumnos, destino=destino, fecha=fecha)
    return redirect('/')



def eliminarExcursion(request, codigo):
    excursion = Excursion.objects.get(codigo=codigo)
    excursion.delete()
    return redirect('/')

def editarExcursion(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    curso = request.POST['txtCurso']
    calumnos = request.POST['numCalumnos']
    destino = request.POST['txtDestino']
    fecha = request.POST['txtFecha']

    excursion = Excursion.objects.get(codigo=codigo)
    excursion.nombre = nombre
    excursion.curso = curso
    excursion.calumnos = calumnos
    excursion.destino = destino
    excursion.fecha = fecha
    excursion.save()
    return redirect('/')

def edicionExcursion(request, codigo):
    excursion = Excursion.objects.get(codigo=codigo)
    return render(request, "edicionExcursion.html", {"excursion": excursion})

from django.shortcuts import render
from django.http import HttpResponse
from App_Coder.models import Curso

# Create your views here.

def curso(self,nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse(f" <p> el curso : {curso.nombre} fue agregado correctamente</p>")

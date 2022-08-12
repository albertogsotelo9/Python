
from django.shortcuts import render
from django.http import HttpResponse
from App_Coder.models import Curso

# Create your views here.

def curso(self,nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse(f" <p> el curso : {curso.nombre} fue agregado correctamente</p>")

def Lista_curso(self):

    lista = Curso.objects.all()
    return render(self, "lista_cursos.html", {"lista_cursos": lista})    

def inicio(self):

    return render(self, "inicio.html")   

def estudiante(self):

    return HttpResponse("visa estudiante")
    
def profesores(self):

    return HttpResponse("visa profes")    

def cursos(self):

    return HttpResponse("visa cursos")   

def entregables(self):

    return HttpResponse("visa entregables")   

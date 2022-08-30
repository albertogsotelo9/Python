
from django.shortcuts import render
from django.http import HttpResponse
from App_Coder.forms import CursoFormulario, ProfesorFormulario
from App_Coder.models import Curso, Profesor

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

    return render(self, "curso.html")  

def entregables(self):

    return HttpResponse("visa entregables")   

# def cursoFormulario(request):

#     print('method:', request.method)
#     print('post:', request.POST)

#     if request.method == 'POST':
#         curso = Curso(nombre=request.POST['curso'], camada = request.POST['camada'])
#         curso.save()
#         return render(request, 'inicio.html')
#     return render(request, "cursoFormulario.html") 

def cursoFormulario(request):
    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(nombre=data['curso'], camada = data['camada'])
            curso.save()
            return render(request, 'inicio.html')

    else:

        miFormulario = CursoFormulario()        
    return render(request, "cursoFormulario.html", {'miFormulario': miFormulario}) 


def busquedaCamada(request):

    return render(request, "busquedaCamada.html") 

def buscar(request):


    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, "resultadoBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        respuesta = "No enviaste datos"    
    return HttpResponse(respuesta) 


def listaProfesores(request):

    profesores = Profesor.objects.all()

    contexto = {"Profesores": profesores}

    return render(request, "leerProfesores.html", contexto)


def crea_profesor(request):
    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data['nombre'], apellido = data['apellido'], email=data['email'],profesion=['profesion'])
            profesor.save()
            return render(request, 'inicio.html')

    else:

        miFormulario = ProfesorFormulario()        
    return render(request, "ProfesorFormulario.html", {'miFormulario': miFormulario})
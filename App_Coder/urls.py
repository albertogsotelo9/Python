from django.urls import path

from App_Coder.views import buscar, busquedaCamada, crea_profesor, curso, Lista_curso, cursos, entregables, estudiante, inicio, listaProfesores, profesores, cursoFormulario

urlpatterns = [
    path('curso/<nombre>/<camada>', curso),
    path('lista-cursos/', Lista_curso),
    path('curso/', cursos, name = 'curso'),
    path('entregables/', entregables),
    path('estudiantes/', estudiante),
    path('profesores/', profesores),
    path('', inicio, name="padre"),
    path('cursoFormulario/', cursoFormulario, name = "cursoFormulario"),
    path('busquedaCamada/', busquedaCamada, name = "BusquedaCamada"),
    path('buscar/', buscar, name = "Busqueda"),
    path('listaProfesores/', listaProfesores, name = "ListaProfesores"),
    path('ProfesorFormulario/', crea_profesor, name = "ProfesorFormulario"),
    
]
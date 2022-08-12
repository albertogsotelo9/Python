from django.urls import path

from App_Coder.views import curso, Lista_curso, entregables, estudiante, inicio, profesores

urlpatterns = [
    path('curso/<nombre>/<camada>', curso),
    path('lista-cursos/', Lista_curso),
    path('curso/', curso),
    path('entregables/', entregables),
    path('estudiantes/', estudiante),
    path('profesores/', profesores),
    path('', inicio),
]
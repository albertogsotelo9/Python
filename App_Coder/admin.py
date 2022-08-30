from django.contrib import admin
from .models import Curso, Entregable, Estudiantes, Profesor
# Register your models here.

class ProfeaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'profesion','email']
    search_fields = ['nombre', 'apellido', 'profesion', 'email']


admin.site.register(Curso)
admin.site.register(Profesor, ProfeaAdmin)
admin.site.register(Estudiantes)
admin.site.register(Entregable)



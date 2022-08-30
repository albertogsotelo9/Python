from django.db import models

# Create your models here.
class Curso(models.Model):
    # nombre = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=50,)
    camada = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.camada}'

    class Meta():
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ('nombre',)
        # ordering = ('nombre','-camada',)
        # ordering = ('-nombre',) 
        unique_together = ('nombre','camada')    

class Estudiantes(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email =   models.EmailField()

    def __str__(self) -> str:
        return f'{self.nombre}  {self.apellido}'

class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email =   models.EmailField()
    profesion =   models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.nombre}  {self.apellido}'

class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado =   models.BooleanField()
    estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f'{self.nombre}  {self.entregado}'

    
from django.db import models

# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    año =  models.DateTimeField(auto_now_add=True)
    genero = models.CharField(max_length=50)


    def __str__(self):
        return self.titulo
    
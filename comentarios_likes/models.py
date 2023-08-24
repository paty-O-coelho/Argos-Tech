from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Comentarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    #caso delete o usuario, apaga todos comentarios dele (cascade)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username
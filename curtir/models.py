from django.db import models
from django.contrib.auth.models import User

class Curtidas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    #caso delete o usuario, apaga todos comentarios dele (cascade)
    curtida = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now_add=True)
    #nao sei se faz sentido mas ok
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.username
from django.db import models
from comentarios_likes.models import Comentarios
from curtir.models import Curtidas

# Create your models here.
class FotosCasamento(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovada = models.BooleanField(default=False)
    
    #a foto vai ter comentarios e curtidas
    comentarios = models.ManyToManyField(Comentarios, blank=True)
    curtidas = models.ManyToManyField(Curtidas, blank=True)
    foto = models.ImageField(upload_to='fotos_casamento', null=True, blank=True)
    def __str__(self):
        return self.nome
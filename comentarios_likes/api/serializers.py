from rest_framework.serializers import ModelSerializer
from comentarios_likes.models import Comentarios

class ComentariosSerializer(ModelSerializer):
    class Meta:
        model = Comentarios
        fields = ('id', 'comentario', 'data', 'aprovado', 'usuario')
        
from rest_framework.viewsets import ModelViewSet
from comentarios_likes.models import Comentarios
from .serializers import ComentariosSerializer

class ComentariosViewSet(ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer
    filter_fields = ('usuario', 'comentario', 'data')
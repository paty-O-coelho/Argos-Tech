from rest_framework.viewsets import ModelViewSet
from curtir.models import Curtidas
from .serializers import CurtidasSerializer

class CurtidasViewSet(ModelViewSet):
    queryset = Curtidas.objects.all()
    serializer_class = CurtidasSerializer
from rest_framework.serializers import ModelSerializer
from curtir.models import Curtidas

class CurtidasSerializer(ModelSerializer):
    class Meta:
        model = Curtidas
        fields = ('id', 'aprovado', 'curtida', 'data', 'usuario')
        #read_only_fields = ('data_criacao', 'data_atualizacao')
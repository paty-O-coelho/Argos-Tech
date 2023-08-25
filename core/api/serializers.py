from rest_framework.serializers import ModelSerializer
from core.models import FotosCasamento

class FotosCasamentoSerializer(ModelSerializer):
    class Meta:
        model = FotosCasamento
        fields = ('id', 'nome', 'descricao' , 'aprovada', 'foto', 'quatidade_de_curtidas',)
        #read_only_fields = ('data_criacao', 'data_atualizacao')
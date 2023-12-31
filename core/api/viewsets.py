from rest_framework.viewsets import ModelViewSet
from core.models import FotosCasamento
from .serializers import FotosCasamentoSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action



#implementar para fazer o crud com o ModelViewSet

class FotosCasamentoViewSet(ModelViewSet):
    #queryset = FotosCasamento.objects.all()
    # CARA COMO VC QUER MOSTRAR ESTE CAMPO?
    serializer_class = FotosCasamentoSerializer

    #quero que so o usuario admin posso autorizar as fotos
    #neste caso para consulta, qualquer um pode ver
    #permission_classes = (IsAdminUser,)
    #authentication_classes = (TokenAuthentication,)

    """
    so vou retornar as fotos que tiverem como aprovação True
    """
    def get_queryset(self):
        """
        ele pode receber este campos por query string
        """
        id_da_foto = self.request.query_params.get('id', None)
        nome_da_foto = self.request.query_params.get('nome', None)
        descricao_da_foto = self.request.query_params.get('descricao', None)
        aprovada = self.request.query_params.get('aprovada', None)
        queryset = FotosCasamento.objects.all()


        """
        nome__icontains
        icontains: não importa se a string esta em maiusculo ou minusculo
        """
        if id_da_foto:
            print(aprovada)
            return queryset.filter(id=id_da_foto)
        elif nome_da_foto:
            return queryset.filter(nome__icontains=nome_da_foto)
        elif descricao_da_foto:
            return queryset.filter(descricao__icontains=descricao_da_foto)
        else:
            """
            se nao receber nenhum destes campos ele retorna apenas as fotos aprovadas
            """
            return queryset.filter(aprovada=True)

    """
    acho que vou usar para editar comentarios nas fotos
    coisa que o instagram não permite hehe
    """
    
     # Método para criar uma nova foto (POST)
    
    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            request.data['aprovada'] = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Método para deletar uma foto (DELETE)
    """
    def destroy(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({"detail": "Você não tem permissão para deletar fotos."}, status=status.HTTP_403_FORBIDDEN)
    """
    #so quem vai poder aprovar a foto é o admin
    @action(methods=['put'], detail=True)
    def associa_likes(self, request, pk):
        if request.user.is_superuser:
            id_da_foto = FotosCasamento.objects.get(id=pk).first()
            id_da_foto.aprovada = request.data['aprovada']
            id_da_foto.save()

    @action(methods=['post'], detail=True)
    def associa_likes(self, request, pk):
        id_da_foto = FotosCasamento.objects.get(id=pk).first()
        id_da_foto.quatidade_de_curtidas += 1
        id_da_foto.save()

    @action(methods=['post'], detail=True)
    def associa_comentarios(self, request, pk):
        id_da_foto = FotosCasamento.objects.get(id=pk).first()
        id_da_foto.comentarios = request.data['comentarios']
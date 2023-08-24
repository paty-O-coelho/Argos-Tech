
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import FotosCasamentoViewSet
from curtir.api.viewsets import CurtidasViewSet
from comentarios_likes.api.viewsets import ComentariosViewSet
from rest_framework.authtoken.views import obtain_auth_token
"""
gambiarra em tempo de desenvolvimento
para poder mostrar as imagens no navegador
"""
from django.conf import settings
from django.conf.urls.static import static




router = routers.DefaultRouter()
router.register(r'fotoscasamento', FotosCasamentoViewSet, basename='FotosCasamento')
router.register(r'curtidas', CurtidasViewSet)
router.register(r'comentarios',ComentariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
quando for feito o deploy da API vamos desconfigurar essas partes
"""
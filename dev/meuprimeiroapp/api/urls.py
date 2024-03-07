from rest_framework.routers import DefaultRouter
# 
from .viewsets import PessoaViewSet
# chama metodos path
from django.urls import include, path

router = DefaultRouter()
# Registra view 
router.register("pessoa", viewset=PessoaViewSet)

# Url, array que contem as definições de rotas
urlpatterns = [
    #/API do url do projeto e /pessoas
    #/api/pessoas
    path("/pessoas", include(router.urls))
]
from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaSerializer
# Importa objeto pesoa banco de dados do models.py
from ..models import PessoaBancoDeDados

class PessoaViewSet(ModelViewSet):
    # Puxa todas as pessoas
    queryset = PessoaBancoDeDados.objects.all()
    serializer_class=PessoaSerializer
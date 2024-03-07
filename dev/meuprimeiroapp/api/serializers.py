from rest_framework.serializers import ModelSerializer
# Importa pessoa banco de dados do models.py
from ..models import PessoaBancoDeDados

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = PessoaBancoDeDados
        # Passa os campos, campo id existe, mas é invisivel
        fields = ['id','primeiro_nome', 'segundo_nome', 'idade']
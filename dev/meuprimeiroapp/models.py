from django.db import models

# Create your models here.

class PessoaBancoDeDados(models.Model):

    # Col name          Models.tipo     verbose_name                      max len
    primeiro_nome = models.CharField(verbose_name="Meu Primeiro Nome", max_length=20)
    segundo_nome = models.CharField(verbose_name="Meu Segundo Nome", max_length=25)
    #                                                       Não obrigatório   false NOT NULL true NULL
    idade = models.IntegerField(verbose_name = "Minha idade", blank=True, null=True)


    def __str__(self) -> str :
        # Define como aparecerá no banco de dados
        return f"{self.primeiro_Wnome} - {self.segundo_nome}"
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class UsuarioModel(models.Model):

    nome = models.CharField(max_length=255, verbose_name='Nome Completo')
    data_Nasc = models.DateField(auto_now=False, verbose_name='Data de Nascimento')
    email = models.EmailField(max_length=300, verbose_name='Email')
    senha = models.CharField(max_length=30 ,verbose_name='Senha de Usuario')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return self.nome


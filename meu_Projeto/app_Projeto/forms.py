from django import forms

from .models import UsuarioModel


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioModel
        fields = ('nome', 'data_Nasc', 'email', 'senha')


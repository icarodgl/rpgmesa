from django import forms
from django.forms import inlineformset_factory

from .models import Chave, Resposta


class RespostaForm(forms.ModelForm):
    class Meta:
        Model = Resposta
        fields = '__all__'
        required_css_class = 'form-control'


class ChaveForm(forms.ModelForm):
    class Meta:
        Model = Chave
        fields = '__all__'

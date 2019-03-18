from django import forms
from django.forms import inlineformset_factory

from .models import Chave, Resposta

class RespostaForm(forms.ModelForm):
    class Meta:
        Model = Resposta
        fields = '__all__'

class ChaveForm(forms.ModelForm):
    class Meta:
        Model = Chave
        fields = '__all__'

RespostaFormSet = inlineformset_factory(Chave, Resposta, form=RespostaForm, extra=2)


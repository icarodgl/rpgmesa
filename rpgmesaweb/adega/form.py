from django import forms
from django.forms import inlineformset_factory, ModelChoiceField

from .models import Venda, Vendedor, Produto
import datetime

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        initial={'nome': int(datetime.datetime.now().strftime('%y%m%d%H%M%s'))}
        fields = '__all__'
        required_css_class = 'form-control'
        

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'
        required_css_class = 'form-control'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        required_css_class = 'form-control'
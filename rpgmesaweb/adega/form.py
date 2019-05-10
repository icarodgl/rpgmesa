from django import forms
from django.forms import inlineformset_factory

from .models import Venda, Vendedor, Produto
import datetime




class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'



    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)


        self.fields['nome'] = forms.CharField(initial=datetime.datetime.today().strftime('%m%d%S'))
        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'disabled':'true'})
        self.fields['vendedor'].widget.attrs.update({'class': 'form-control'})
        self.fields['produto'].widget.attrs.update({'class': 'form-control'})
        self.fields['data'] = forms.DateField(initial=datetime.date.today)
        self.fields['data'].widget.attrs.update({'class': "form-control", 'data-date-format': "DD-MM-YYYY"})


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'



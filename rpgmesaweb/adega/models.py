from django.db import models
from django.contrib.auth.models import User


class Vendedor(User):
    nome = models.CharField(max_length=200)
    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    valor = models.FloatField(default=0)
    estoque = models.IntegerField(default=0)

    def __str__(self):
        return self.nome + ': ' + self.descricao


class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data = models.DateField('data')

    def __str__(self):
        return self.vendedor.nome

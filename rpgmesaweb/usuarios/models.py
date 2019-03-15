from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    criado = models.DateTimeField('date published')

    def __str__(self):
        return self.nome


class Frase(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.texto

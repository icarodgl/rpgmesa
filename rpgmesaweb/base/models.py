from django.db import models


class Chave(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Resposta(models.Model):
    chave = models.ForeignKey(Chave, on_delete=models.CASCADE)
    resposta = models.CharField(max_length=200)
    frequencia = models.IntegerField(default=1)

    def __str__(self):
        return self.resposta

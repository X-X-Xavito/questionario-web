from django.db import models

# Create your models here.

class Questionario(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto
from django.db import models

# Create your models here.

"""
    Criação de três modelos no banco de dados. Cada modelo tem atributo.
    Pergunta e Alternativa tem ForeignKey que define que esses modelos são atributos de outro modelo.
    Metodo__str__ serve para exibir o objeto para o usuario
    ImagemField serve para definir um atributo com imagem, sendo que a imagem padrão é 'python.jpg'
"""


class Questionario(models.Model):
    titulo = models.CharField(max_length=200)
    contador = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class Pergunta(models.Model):
    questionario = models.ForeignKey(Questionario, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    imagem = models.ImageField(default="python.jpg")

    def __str__(self):
        return self.texto

class Alternativa(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto
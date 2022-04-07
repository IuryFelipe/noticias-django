from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField("Título", max_length=128)
    conteudo = models.TextField("Conteúdo")
    data_de_pubicacao = models.DateField("Data de publicação", blank=True, null=True)
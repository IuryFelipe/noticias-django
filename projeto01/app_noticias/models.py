from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField("Título", max_length=128, null = True, blank = True)
    conteudo = models.TextField("Conteúdo")
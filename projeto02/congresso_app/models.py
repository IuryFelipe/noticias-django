from django.db import models

class Pessoa(models.Model):
    nome =  models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.nome

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=50, blank=True, null=True)
    razaoSocial = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)
    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        verbose_name='Estado',
        null=True,
        blank=True)
    def __str__(self):
        return self.nome

class PalavraChave(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    eventoPrincipal = models.CharField(max_length=100, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)
    dataEHoraDeInicio = models.DateTimeField('Data e  hora de início', blank=True, null=True)
    logotipo = models.CharField(max_length=1000, blank=True, null=True)
    endereco = models.CharField(max_length=500, blank=True, null=True)
    cep = models.CharField(max_length=50, blank=True, null=True)
    palavrasChave = models.ManyToManyField(PalavraChave)
    realizador = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        verbose_name='Relizador', 
        blank=True, null=True)
    def __str__(self):
        return self.nome

class EventoCientifico(Evento):
    issn = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.nome

class Autor(Pessoa):
    curriculo = models.TextField(max_length=2000, blank=True, null=True)
    def __str__(self):
        return self.nome 

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    evento = models.ForeignKey(
        EventoCientifico,
        on_delete=models.CASCADE,
        verbose_name='Evento',
        blank=True, null=True)
    autores = models.ManyToManyField(Autor, blank=True)
    def __str__(self):
        return self.titulo
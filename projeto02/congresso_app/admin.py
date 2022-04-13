from django.contrib import admin

from .models import *

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    pass

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    pass

@admin.register(PalavraChave)
class PalavraChaveAdmin(admin.ModelAdmin):
    pass

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    pass

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    pass

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

@admin.register(EventoCientifico)
class EventoCientificoAdmin(admin.ModelAdmin):
    pass

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtigoCientifico)
class ArtigoCientificoAdmin(admin.ModelAdmin):
    pass
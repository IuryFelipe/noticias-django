from django.contrib import admin
from .models import Noticia
from .models import Pessoa

# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    pass

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    pass
from django.http import HttpResponse
from django.shortcuts import render

from app_noticias.models import Pessoa

def resumo_pessoas(request):
    total = Pessoa.objects.count()
    return HttpResponse('O total de pessoas é {}' .format(total))

def index(request):
    return HttpResponse('Página inicial')

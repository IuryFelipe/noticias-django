from app_noticias.views import index
from app_noticias.views import resumo_pessoas
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('pessoas', resumo_pessoas)
]

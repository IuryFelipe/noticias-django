# Generated by Django 4.0.3 on 2022-04-01 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=128, null=True, verbose_name='Título')),
                ('conteudo', models.TextField(verbose_name='Conteúdo')),
            ],
        ),
    ]

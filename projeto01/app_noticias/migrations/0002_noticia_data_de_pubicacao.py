# Generated by Django 4.0.3 on 2022-04-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='data_de_pubicacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de publicação'),
        ),
    ]

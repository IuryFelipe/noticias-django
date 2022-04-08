# Generated by Django 4.0.3 on 2022-04-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_noticias', '0004_noticia_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='tags',
            field=models.ManyToManyField(to='app_noticias.tag'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congresso_app', '0005_autor_alter_evento_realizador_artigocientifico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='curriculo',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
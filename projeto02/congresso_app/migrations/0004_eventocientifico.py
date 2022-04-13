# Generated by Django 4.0.3 on 2022-04-11 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('congresso_app', '0003_cidade_estado_cidade_nome_estado_nome_estado_sigla_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='congresso_app.evento')),
                ('issn', models.CharField(blank=True, max_length=20, null=True)),
            ],
            bases=('congresso_app.evento',),
        ),
    ]

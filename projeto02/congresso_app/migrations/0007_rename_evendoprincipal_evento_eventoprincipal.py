# Generated by Django 4.0.3 on 2022-04-11 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('congresso_app', '0006_alter_autor_curriculo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='evendoPrincipal',
            new_name='eventoPrincipal',
        ),
    ]

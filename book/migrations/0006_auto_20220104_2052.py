# Generated by Django 3.2.6 on 2022-01-04 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20220104_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carti',
            old_name='id_autor',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='carti',
            old_name='id_biblioteca',
            new_name='iblioteca',
        ),
    ]

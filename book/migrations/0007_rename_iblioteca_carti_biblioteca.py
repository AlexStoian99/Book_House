# Generated by Django 3.2.6 on 2022-01-04 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20220104_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carti',
            old_name='iblioteca',
            new_name='biblioteca',
        ),
    ]

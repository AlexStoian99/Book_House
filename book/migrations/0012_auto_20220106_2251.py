# Generated by Django 3.2.6 on 2022-01-06 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_alter_carti_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'permissions': [('can_delete_authors', 'You can delete authors.')]},
        ),
        migrations.AlterModelOptions(
            name='biblioteca',
            options={'permissions': [('can_delete_libraries', 'You can delete libraries.')]},
        ),
    ]

# Generated by Django 3.2.6 on 2022-01-06 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20220107_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biblioteca',
            options={'permissions': [('can_delete_libraries', 'You can delete libraries.')]},
        ),
        migrations.AlterModelOptions(
            name='carti',
            options={'permissions': [('can_delete_books', 'You can delete books.')]},
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-14 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chilestay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='pais',
        ),
        migrations.DeleteModel(
            name='Pais',
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-21 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chilestay', '0002_remove_region_pais_delete_pais'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo_electronico',
            field=models.EmailField(default='default@example.com', max_length=255),
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chilestay', '0007_inmueble_capacidad_adultos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='inmuebles/'),
        ),
    ]

# Generated by Django 4.0.6 on 2024-06-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0008_director_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='foto',
        ),
        migrations.AddField(
            model_name='director',
            name='fotoD',
            field=models.FileField(blank=True, null=True, upload_to='directores'),
        ),
    ]

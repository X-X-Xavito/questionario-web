# Generated by Django 2.1.5 on 2019-01-22 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0002_auto_20190122_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='imagem',
            field=models.ImageField(default='python.jpg', upload_to=''),
        ),
    ]

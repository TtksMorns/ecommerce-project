# Generated by Django 5.1.3 on 2025-01-09 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0008_produto_data_produto_localizacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='data',
            field=models.DateTimeField(default='2025-01-01T00:00:00'),
        ),
    ]

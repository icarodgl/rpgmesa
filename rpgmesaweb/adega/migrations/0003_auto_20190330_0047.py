# Generated by Django 2.1.7 on 2019-03-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adega', '0002_auto_20190329_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='venda',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]

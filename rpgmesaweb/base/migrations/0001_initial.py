# Generated by Django 2.1.7 on 2019-03-16 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resposta', models.CharField(max_length=200)),
                ('frequencia', models.IntegerField(default=1)),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Chave')),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-06 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaBancoDeDados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=20, verbose_name='Meu Primeiro Nome')),
                ('segundo_nome', models.CharField(max_length=25, verbose_name='Meu Segundo Nome')),
                ('idade', models.IntegerField(blank=True, null=True, verbose_name='Minha idade')),
            ],
        ),
    ]

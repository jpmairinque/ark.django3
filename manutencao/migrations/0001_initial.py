# Generated by Django 2.2.24 on 2021-09-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.IntegerField()),
                ('nome', models.CharField(max_length=50)),
                ('nome_fantasia', models.CharField(max_length=50)),
                ('superior', models.CharField(max_length=50)),
                ('cnpj', models.CharField(max_length=50)),
                ('observacoes', models.CharField(max_length=50)),
                ('contato', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('telefone2', models.CharField(max_length=50)),
                ('ramal2', models.CharField(max_length=50)),
                ('telefone1', models.CharField(max_length=50)),
                ('ramal1', models.CharField(max_length=50)),
                ('fax', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]
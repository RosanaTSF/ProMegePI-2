# Generated by Django 5.1.1 on 2024-10-14 01:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0009_alter_phonecontact_contact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResquestSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(verbose_name='Data da Requisição')),
                ('reson_hiring', models.CharField(max_length=254, verbose_name='Motivo da Contratação')),
                ('contract_value', models.FloatField(verbose_name='Valor Total do Contrato')),
                ('status', models.CharField(choices=[('IT', 'Iniciado'), ('PL', 'Paralizado'), ('IP', 'Em andamento'), ('FN', 'Finalizado'), ('CP', 'Concluido')], default='IT', max_length=2, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Requisição ao Fornecedor',
                'verbose_name_plural': 'Requisições aos Fornecedores',
            },
        ),
        migrations.CreateModel(
            name='AddressSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=9, verbose_name='CEP')),
                ('address', models.CharField(max_length=100, verbose_name='Lougradouro')),
                ('district', models.CharField(max_length=70, verbose_name='Bairro')),
                ('city', models.CharField(max_length=70, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='UF')),
                ('ibge_code', models.CharField(max_length=10, verbose_name='Código IBGE')),
                ('gia_code', models.CharField(max_length=6, verbose_name='Código GIA')),
                ('ddd_code', models.CharField(max_length=2, verbose_name='Código DDD')),
                ('siafi_code', models.CharField(max_length=6, verbose_name='Código SIAFI')),
                ('address_type', models.CharField(choices=[('RS', 'Residencial'), ('CM', 'Comercial'), ('OT', 'Outros')], max_length=2, verbose_name='Tipo de Endereço')),
                ('number', models.CharField(max_length=5, verbose_name='Número')),
                ('complement', models.CharField(max_length=20, verbose_name='Complemento')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier', verbose_name='Fornecedor')),
            ],
            options={
                'verbose_name': 'Endereço do Fornecedor',
                'verbose_name_plural': 'Endereços dos Fornecedores',
            },
        ),
    ]
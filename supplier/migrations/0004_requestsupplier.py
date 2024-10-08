# Generated by Django 5.1.1 on 2024-09-21 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_delete_requestsupplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(verbose_name='Data da Requisição')),
                ('reson_hiring', models.CharField(max_length=254, verbose_name='Motivo da Contratação')),
                ('contract_value', models.FloatField(verbose_name='Valor Total do Contrato')),
                ('status', models.CharField(choices=[('IT', 'Iniciado'), ('PL', 'Paralizado'), ('IP', 'Em andamento'), ('FN', 'Finalizado'), ('CP', 'Concluido')], default='IT', max_length=2, verbose_name='Status')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier', verbose_name='Fornecedor')),
            ],
            options={
                'verbose_name': 'Requisição ao Fornecedor',
                'verbose_name_plural': 'Requisições aos Fornecedores',
            },
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-01 22:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppli_request', '0002_remove_suppliresquest_created_by_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplyResquest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('date_request', models.DateField(verbose_name='Data da Requisição')),
                ('description_request', models.CharField(max_length=150, verbose_name='Descrição da Requisição')),
                ('status', models.CharField(choices=[('ST', 'Iniciado'), ('IP', 'Em Andamento'), ('CS', 'Fechado'), ('CP', 'Finalizado'), ('CC', 'Cancelado')], max_length=2, verbose_name='Status')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Requisição de Fornecimento',
                'verbose_name_plural': 'Requisições de Fornecimento',
            },
        ),
        migrations.CreateModel(
            name='ItensSupplyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_item_request', models.CharField(max_length=30, verbose_name='Código do Item Requisitado')),
                ('description_item', models.CharField(max_length=200, verbose_name='Descrição do Item Requisitado')),
                ('amount_item', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('unit_measurement', models.CharField(choices=[('UNI', 'Unidade'), ('BOX', 'Caixa'), ('KG', 'Kilograma'), ('BCK', 'Balde'), ('TRY', 'Bandeja'), ('BAR', 'Barra'), ('BLK', 'Bloco'), ('BOB', 'Bobina'), ('CAPS', 'Capsula'), ('CART', 'Cartela'), ('HUNDRED', 'Cento'), ('SET', 'Conjuento'), ('CM', 'Centimetro'), ('CM2', 'Centrimetro Quadrado'), ('DISP', 'Display'), ('DOZEN', 'Duzia'), ('PACKAGE', 'Embalagem'), ('BALE', 'Fardo'), ('SHEET', 'Folha'), ('GALLON', 'Galão'), ('GF', 'Frasco'), ('GRAMS', 'Gramas'), ('GAME', 'Jogo'), ('KIT', 'Kit'), ('CAN', 'Lata'), ('LITER', 'Litro'), ('M', 'Metro'), ('M2', 'Metro Quadrado'), ('M3', 'Metro Cúbico'), ('THOUSAND', 'Milheiro'), ('ML', 'Mililitro'), ('MWH', 'MegaWhats/Hora'), ('PALLET', 'Palete'), ('PAIRS', 'Pares'), ('PC', 'Peça'), ('POT', 'Pote'), ('K', 'Kilate'), ('REAM', 'Resma'), ('ROLL', 'Rolo'), ('BAG', 'Saco'), ('DRUM', 'Tambor'), ('TANK', 'Tanque'), ('TON', 'Tonelada'), ('TUBE', 'Tubo'), ('VESL', 'Vasilhame'), ('GLASS', 'Vidro')], max_length=8, verbose_name='Unidade')),
                ('unit_value', models.FloatField(verbose_name='Valor Unitãrio')),
                ('supply_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suppli_request.supplyresquest', verbose_name='Requisição de Fornecimento')),
            ],
            options={
                'verbose_name': 'ItensSupplyRequest',
                'verbose_name_plural': 'ItensSupplyRequests',
            },
        ),
    ]

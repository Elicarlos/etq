# Generated by Django 4.1.5 on 2023-01-25 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('cnpj', models.CharField(max_length=100)),
                ('razao', models.CharField(max_length=100)),
                ('filial', models.CharField(max_length=100)),
                ('sif_sie', models.CharField(max_length=100)),
                ('registro_adapi', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('descricao', models.CharField(max_length=100, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('codigo_barras', models.CharField(max_length=100, null=True)),
                ('temperatura', models.CharField(max_length=100, null=True)),
                ('sexo', models.CharField(max_length=100, null=True)),
                ('valor_energetico', models.CharField(max_length=100, null=True)),
                ('carboidratos', models.CharField(max_length=100, null=True)),
                ('proteinas', models.CharField(max_length=100, null=True)),
                ('gorduras_totais', models.CharField(max_length=100, null=True)),
                ('gorduras_saturadas', models.CharField(max_length=100, null=True)),
                ('colesterol', models.CharField(max_length=100, null=True)),
                ('fibra_alimentar', models.CharField(max_length=100, null=True)),
                ('calcio', models.CharField(max_length=100, null=True)),
                ('ferro', models.CharField(max_length=100, null=True)),
                ('sodio', models.CharField(max_length=100, null=True)),
                ('gordura_trans', models.CharField(max_length=100, null=True)),
                ('vd1', models.CharField(max_length=100, null=True)),
                ('vd2', models.CharField(max_length=100, null=True)),
                ('vd3', models.CharField(max_length=100, null=True)),
                ('vd4', models.CharField(max_length=100, null=True)),
                ('vd5', models.CharField(max_length=100, null=True)),
                ('vd6', models.CharField(max_length=100, null=True)),
                ('vd7', models.CharField(max_length=100, null=True)),
                ('vd8', models.CharField(max_length=100, null=True)),
                ('ingredientes', models.TextField(max_length=1000, null=True)),
                ('gluten', models.TextField(max_length=100, null=True)),
                ('lactose', models.TextField(max_length=100, null=True)),
                ('lote', models.TextField(max_length=100, null=True)),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.tipo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
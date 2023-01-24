from django.db import models

# Create your models here.

class Base(models.Model):
    pass


class Tipo(Base):
    descricao = models.CharField()


class Produto(models):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=)
    codigo_barras = models.CharField()
    temperatura = models.CharField()
    sexo = models.CharField()
    valor_energetico = models.CharField()
    carboidratos
    proteinas
    gorduras
    totais
    gorduras
    saturadas
    colesterol
    fibra
    alimentar	
    calcio
    ferro
    sodio
    gordura_trans
    %vd1
    %vd2
    %vd3
    %vd4
    %vd5
    %vd6
    %vd7
    %vd8
    ingredientes
    gluten
    lactose
    lote






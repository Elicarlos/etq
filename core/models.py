from django.db import models

# Create your models here.

class Base(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    

class Empresa(Base):
    cnpj = models.CharField(max_length=100)
    razao = models.CharField(max_length=100)
    filial = models.CharField(max_length=100)
    sif_sie = models.CharField(max_length=100)
    registro_adapi = models.CharField(max_length=100)

class Tipo(Base):
    descricao = models.CharField(max_length=100)


class Produto(Base):
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, null=True)
    codigo = models.IntegerField(unique=True ,null=True)
    descricao = models.CharField(max_length=100,null=True)
    preco = models.DecimalField(max_digits=10000, decimal_places=2)
    codigo_barras = models.CharField(max_length=100,null=True)
    temperatura = models.CharField(max_length=100,null=True)
    sexo = models.CharField(max_length=100,null=True)
    valor_energetico = models.CharField(max_length=100,null=True)
    carboidratos = models.CharField(max_length=100,null=True)
    proteinas = models.CharField(max_length=100,null=True)
    gorduras_totais = models.CharField(max_length=100,null=True)    
    gorduras_saturadas = models.CharField(max_length=100,null=True)
    colesterol = models.CharField(max_length=100,null=True)
    fibra_alimentar = models.CharField(max_length=100,null=True)
    calcio = models.CharField(max_length=100,null=True)
    ferro = models.CharField(max_length=100,null=True)
    sodio = models.CharField(max_length=100,null=True)
    gordura_trans = models.CharField(max_length=100,null=True)
    vd1 = models.CharField(max_length=100,null=True)
    vd2 = models.CharField(max_length=100,null=True)
    vd3 = models.CharField(max_length=100,null=True)
    vd4 = models.CharField(max_length=100,null=True)
    vd5 = models.CharField(max_length=100,null=True)
    vd6 = models.CharField(max_length=100,null=True)
    vd7 = models.CharField(max_length=100,null=True)
    vd8 = models.CharField(max_length=100,null=True)
    ingredientes = models.TextField(max_length=1000,null=True)
    gluten = models.TextField(max_length=100,null=True)
    lactose = models.TextField(max_length=100,null=True)
    lote = models.TextField(max_length=100,null=True)








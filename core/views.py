from django.shortcuts import render
from . models import Produto, Tipo, Empresa


# Create your views here.


def impressao(request):
    context ={}
    return render(request, 'core/impressao.html', context)


# def gerar_etiqueta(request, id):
#     produto = Produto.objects.get(id=id)
#     print(produto.descricao)
    





from django.shortcuts import render
from . models import Produto, Tipo, Empresa



# Create your views here.

def buscar_produto(request, texto):
    query =  Produto.objects.filter(descricao__contains=texto)
    return render(request, 'core/impressao.html', query)



def impressao(request):
    context ={}
    return render(request, 'core/impressao.html', context)


# def gerar_etiqueta(request, id):
#     produto = Produto.objects.get(id=id)
#     print(produto.descricao)
    





# Create your views here.

# def gerar_etiqueta(request, id):
#     produto = Produto.objects.get(id=id)
#     print(produto.descricao)
    


# gerar_etiqueta()


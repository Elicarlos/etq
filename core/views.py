from django.shortcuts import render
from . models import Produto, Tipo, Empresa
from . forms import FormSearch
from django.db.models import Q



# Create your views here.

def buscar(request):
    if request.method == 'POST':
        
        form = FormSearch(request.POST)
        if form.is_valid():           
            query = form.cleaned_data['buscar']      
            produtos = Produto.objects.filter(
                Q(codigo__contains=query) | Q(codigo_barras__contains=query)
            ) 

            return render(request, 'core/busca_resultado.html',{'result': produtos})
        
       

    else:
        form = FormSearch()
    
    return render(request, 'core/busca.html', {'form': form})


def listar_produtos(request):
    return render(request, )






# def impressao(request):
#     context ={}
#     return render(request, 'core/impressao.html', context)


# def gerar_etiqueta(request, id):
#     produto = Produto.objects.get(id=id)
#     print(produto.descricao)
    





# Create your views here.

# def gerar_etiqueta(request, id):
#     produto = Produto.objects.get(id=id)
#     print(produto.descricao)
    


# gerar_etiqueta()


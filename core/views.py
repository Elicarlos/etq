from django.shortcuts import render
from . models import Produto, Tipo, Empresa
from . forms import FormSearch
from django.db.models import Q



# Create your views here.

def index(request):
    if request.method == 'POST':
        
        form = FormSearch(request.POST)
        
        
        if form.is_valid():           
            query = request.POST.get('buscar')
             
            produtos = Produto.objects.filter(
                Q(codigo__exact=query) | Q(codigo_barras__exact=query)
            ) 

            return render(request, 'core/index.html',{'produtos': produtos,'query': query})
        
       

    else:
        form = FormSearch()
    
    return render(request, 'core/index.html', {'form': form})



    
    # return render(request, 'core/index.html')

def cadastro_produtos(request):
    contexto = {
        'formCadastroProdutos': 'teste'
    }
    return render(request, 'core/cadastro-produtos.html', contexto)

def buscar(request):
    if request.method == 'POST':
        print(request.POST.get('buscar'))
        
        form = FormSearch(request.POST)
        if form.is_valid():           
            query = form.cleaned_data['buscar']
            print(query)      
            produtos = Produto.objects.filter(
                Q(codigo__contains=query) | Q(codigo_barras__contains=query)
            ) 

            return render(request, 'core/index.html',{'produtos': produtos,'query': query})
        
       

    else:
        form = FormSearch()
    
    return render(request, 'core/busca.html', {'form': form})


def listar_produtos(request):
    contexto = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'core/lista-produtos.html', contexto )






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


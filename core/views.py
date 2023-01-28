from django.shortcuts import render
from . models import Produto, Tipo, Empresa
from . forms import FormSearch



# Create your views here.

def buscar(request):
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():           
            query = form.changed_data['buscar']       
            result = Produto.objects.filter(codigo__contains==query or codigo_barras__contains==query)
            return render(request, 'core/busca_resultado.html',{'resultado': result})
        
       

    else:
        form = FormSearch()
    
    return render(request, 'core/busca.html', {'form': form})



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


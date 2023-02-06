from django.shortcuts import redirect, render, HttpResponse
from . models import Produto, Tipo, Empresa
from . forms import FormSearch, FormPrint
from django.db.models import Q
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape, A4
from reportlab.lib.units import cm
from datetime import datetime
import win32print
import win32api
from io import BytesIO


# Create your views here.

# def index(request):
#     print('Estou dentro do Index')
#     if request.method == 'POST':
#         print('Estou dentro do Index')
#         print('Este é o formPrint>>>>>>>', dir(FormPrint))        
#         form = FormSearch(request.POST)       
#         if form.is_valid():           
#             query = request.POST.get('buscar')             
#             produtos = Produto.objects.filter(
#                 Q(codigo__exact=query) | Q(codigo_barras__exact=query)
#             ) 
#             print('Este é o formPrint>>>>>>>', dir(FormPrint))
#             return render(request, 'core/index.html',{'produtos': produtos,'query': query, 'FormPrint': FormPrint})
        
       

#     else:
#         form = FormSearch()
#         print('Este é o formPrint>>>>>>>', dir(FormPrint))    
        
#     return render(request, 'core/index.html', {'form': form})



    
    # return render(request, 'core/index.html')

def cadastro_produtos(request):
    contexto = {
        'formCadastroProdutos': 'teste'
    }
    return render(request, 'core/cadastro-produtos.html', contexto)

def index(request):    
    if request.method == 'POST':
        form = FormSearch(request.POST)
        if form.is_valid():
            query = form.cleaned_data['buscar'] 
            try:       
            
                produtos = Produto.objects.filter(
                    Q(codigo__exact=query) | Q(codigo_barras__exact=query)
                )
                              
                            
                return render(request, 'core/index.html',{'produtos': produtos, 'form': form, 'FormPrint': FormPrint})
            
            except Produto.DoesNotExist:
                return render(request, 'core/index.html', {'form': form, 'error_message': 'Produto não encontrado.'})

    else:   
        return render(request, 'core/index.html')
    return render(request, 'core/index.html', {'form': form})


def listar_produtos(request):
    contexto = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'core/lista-produtos.html', contexto )


def printer(request):
    
    if request.method == 'POST':
        
        form = FormPrint(request.POST)
        if form.is_valid():
            printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
            
            id = form.cleaned_data['id']
            produto = Produto.objects.get(id=id)           
            tipo = form.cleaned_data['tipo']
            descricao = form.cleaned_data['descricao']
            data_embalagem = form.cleaned_data['data_embalagem']          
            data_embalagem = data_embalagem.strftime("%d/%m/%Y")   
           
            
            validade = form.cleaned_data['validade']
            validade = validade.strftime("%d/%m/%Y")
            quantidade = form.cleaned_data['quantidade']
            impressora_selecionada = form.cleaned_data['printer']
           

            chosen_label = form.cleaned_data['label']
            # id_produto = form.cleaned_data['id-produto']
         
            # Use a switch statement or if/elif blocks to determine which label to generate
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="label.pdf"'
            response = BytesIO(response.content)
                    
            if chosen_label == 'label1':
                # buffer = BytesIO()
                pagesize = (9*cm, 14*cm) # 10x30 cm 
                canvas_obj = canvas.Canvas(response, pagesize=pagesize)
                for i in range(quantidade):                   
                                
                    canvas_obj.drawCentredString(4*cm, 12*cm, descricao)
                    canvas_obj.drawString(4*cm, 11*cm, data_embalagem)
                    canvas_obj.drawCentredString(4*cm, 10*cm, validade)
                    canvas_obj.drawCentredString(4*cm, 9*cm, descricao)
                    canvas_obj.drawCentredString(4*cm, 9*cm, tipo)
                    canvas_obj.drawCentredString(4*cm, 9*cm, produto.calcio)
                    canvas_obj.showPage()
                canvas_obj.save()
                # return response
               
                # return response
             

                if impressora_selecionada in [printer[2] for printer in printers]:
                    # Open the selected printer
                    handle = win32print.OpenPrinter(impressora_selecionada)
                    win32print.StartDocPrinter(handle, 1, ("Test Document", None, "RAW"))
                    win32print.WritePrinter(handle, response.getvalue())
                    win32print.EndDocPrinter(handle)
                    win32print.ClosePrinter(handle)
                    return redirect('home')
                    # print(impressora_selecionada)
                    # win32print.SetDefaultPrinter(impressora_selecionada)

                    # win32api.ShellExecute(0, 'print', canvas_obj, None, None, 0 )
                #     handle = win32print.OpenPrinter(impressora_selecionada)
                   

                #     # Start the document
                #     win32print.StartDocPrinter(handle, 1, ("Test Document", None, "RAW"))
                    
                #     # Write the data to the printer
                #     win32print.WritePrinter(handle, canvas_obj)

                #     # End the document
                #     win32print.EndDocPrinter(handle)

                #     # Close the printer handle
                #     # win32print.ClosePrinter(handle)
                # else:
                    print("The selected printer is not installed")
                # win32print.StartDocPrinter(printer, 1, ("test_job", None, "RAW"))
                # win32print.WritePrinter(printer, canvas_obj.getvalue())
                # win32print.EndDocPrinter(printer)
                # return response
                # Generate label 1
            elif chosen_label == 'label2':
                pass
                # Generate label 2
            elif chosen_label == 'label3':
                # Generate label 3
            # Continue to send the generated label
                pass

        else:
            print('Formulario invalido')
    else:
        form = FormPrint()
    return render(request, 'core/index.html', {'form': form})




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


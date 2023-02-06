from django import forms
import win32print

class FormSearch(forms.Form):
    buscar = forms.IntegerField(label='Buscar')


class FormPrint(forms.Form):
    id = forms.IntegerField()   
    tipo = forms.CharField()
    descricao = forms.CharField()
    data_embalagem = forms.DateField()
    validade  = forms.DateField()
    quantidade = forms.IntegerField()
    printer = forms.ChoiceField(label='Printer')
    label_choices = (
        ('label1', 'Frente - Impressora Zebra'),
        ('label2', 'Etiqueta 2'),
        ('label3', 'Etiqueta 3'),
    )
    label = forms.ChoiceField(choices=label_choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL)
        self.fields['printer'].choices = [(p[2], p[2]) for p in printers]

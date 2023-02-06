from django.urls import path
from . import views


urlpatterns = [
    # path('impressao/', views.impressao, name="impressao"),
    path('', views.index, name='home'),
    # path('buscar/', views.buscar, name='buscar'),
    path('cadastro-produtos/', views.cadastro_produtos, name='cadastro-produtos'),
    path('lista-produtos/', views.listar_produtos, name='lista-produtos'),
    path('printer/', views.printer, name='printer'),
    # path('lista-produtos/', views.listar_produtos, neme='lista-produtos'),
    
]
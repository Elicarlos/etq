from django.urls import path
from . import views


urlpatterns = [
    # path('impressao/', views.impressao, name="impressao"),
    path('buscar/', views.buscar, name='buscar'),
    # path('lista-produtos/', views.listar_produtos, neme='lista-produtos'),
    
]
from django.urls import path
from . import views


urlpatterns = [
    path('impressao/', views.impressao, name="impressao"),
    
]
from django.urls import path
from .views import Home, EsPrimoWS

urlpatterns = [
    path('', Home , name='home'),
    path('ws/es_primo/', EsPrimoWS, name='es_primo'),
]
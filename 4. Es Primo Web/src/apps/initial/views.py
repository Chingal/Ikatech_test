from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from .tasks import add, es_primo
import json

def Home(request):
    title = "Calcular Número Primo"
    return render(request, 'initial/index.html', locals())

def EsPrimoWS(request):
    numero = request.GET.get('numero')
    if numero:        
        primo = es_primo.delay(int(numero))
    data = {
        'es_primo' : primo.get(), 
        'numero': numero
    }    
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Página de Clientes")
    return render(request, 'clientes/index.html')

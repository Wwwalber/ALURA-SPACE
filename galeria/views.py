from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Alura Space!</h1><p>Bem vindo ao espaço</p>")

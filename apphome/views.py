from django.shortcuts import render
from .forms import ContatoForm


def index_home(request):
    return render(request, 'index.html')


def contato(request):
    return render(request, 'contato.html')


def produto(request):
    return render(request, 'produto.html')



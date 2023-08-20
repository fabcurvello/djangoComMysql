from django.shortcuts import render
from .forms import ContatoForm


def index_home(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm()

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)




def produto(request):
    return render(request, 'produto.html')



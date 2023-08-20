from django.contrib import messages
from django.shortcuts import render

from .forms import ContatoForm


def index_home(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None) # ou recebe o que o usuário vai enviar ou none que é quando a página é carregada ainda vazia

    if (str(request.method) == 'POST'):
        if (form.is_valid()):
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print(f"-- Mensagem eviada: \nNome: {nome} \nE-mail: {email} \nAssunto: {assunto} \nMensagem: {mensagem} \n--")

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')






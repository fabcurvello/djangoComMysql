from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto


def index_home(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None) # ou recebe o que o usuário vai enviar ou none que é quando a página é carregada ainda vazia

    if (str(request.method) == 'POST'):
        if (form.is_valid()):
            '''
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print(f"\n-- Mensagem eviada: \nNome: {nome} \nE-mail: {email} \nAssunto: {assunto} \nMensagem: {mensagem} \n--")
            '''

            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    print(f"Usuário: {request.user}")
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES) # Files pq tem as imagens, que são arquivos.
            if (form.is_valid()):
                # prod = form.save(commit=False) # Provisório
                # print(f"Nome: {prod.nome}")
                # print(f"Preço: {prod.preco}")
                # print(f"Estoque: {prod.estoque}")
                # print(f"Imagem: {prod.imagem}")

                form.save()

                messages.success(request, "Produto salvo com sucesso!")
                form = ProdutoModelForm() # limpar campos do form
            else:
                messages.error(request, "Erro ao cadastrar produto!")
        else:
            form = ProdutoModelForm()
        context = {
            "form": form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')









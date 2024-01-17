from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm
from base.models import Contato, Reserva



def inicio(request):
    return render(request, 'inicio.html')

'''def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
            sucesso = True
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            Contato.objects.create(nome=nome, email=email, mensagem=mensagem)
    resposta = {
        'telefone': '(16) 9999-9999',
        'responsavel': 'Maria Silva',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', resposta)'''

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    resposta = {
        'telefone': '(16) 9999.9999',
        'responsavel': 'Maria da Silva Pereira',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', resposta)
        

def reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()
    resposta = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'reserva.html', resposta)
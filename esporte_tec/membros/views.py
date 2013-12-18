# -*- coding: utf-8 -*
from django.shortcuts import redirect

from annoying.decorators import render_to

from esporte_tec.membros.models import *

from esporte_tec.membros.forms import EmpresaForm
from esporte_tec.membros.forms import ColaboradorForm
from esporte_tec.membros.forms import AcademiaForm
from esporte_tec.membros.forms import GovernoForm


@render_to("cadastro_empresa.html")
def cadastrar_empresa(request):

    if request.method == 'POST':
        # pega os dados do post e joga no form
        form = EmpresaForm(request.POST)

        # se for valido salva e redireciona
        if form.is_valid():
            form.save()
            # criar uma pagina de "cadastro realizado com sucesso e redirecionar para ela no lugar da home
            return redirect('sucesso')

    else:
        # cria um formulario em branco
        form = EmpresaForm()

    # se for invalido carrega a mesma pagina mas nesse ponto a variavel form já foi validada e portanto vai
    # ter os dados dos erros do formulario

    # Se chegou aqui é por que ou foi um GET, e portanto o form está vazio, ou foi
    # um post mas com erros de validação no form. Assim vai carregar o template indicado, com os dados do
    # form (vazio se for GET ou form com erros se for invalido)
    return {
        'form': form,
    }

@render_to("cadastro_colaborador.html")
def cadastrar_colaborador(request):

    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        form.save()

        return redirect('sucesso')

    else:
        form = ColaboradorForm()

    return{
        'form': form,
    }

@render_to("cadastro_academia.html")
def cadastrar_instituicao_academica(request):

    if request.method == 'POST':
        form = AcademiaForm(request.POST)
        form.save()

        return redirect('sucesso')

    else:
        form = AcademiaForm()

    return{
        'form': form,
    }

@render_to("cadastro_governo.html")
def cadastrar_instituicao_governamental(request):

    if request.method == 'POST':
        form = GovernoForm(request.POST)
        form.save()

        return redirect('sucesso')

    else:
        form = GovernoForm()

    return{
        'form': form,
    }


def _get_dados_listar_membros(tipo_membro):
    membros = []
    titulo_membros = ""
    if tipo_membro == 'empresa':
        membros = Empresa.objects.all()
        titulo_membros = "Empresas"

    return {'membros' : membros, 'titulo_membros' : titulo_membros}

@render_to("listagem_membro.html")
def listar_membros(request, tipo_membro):

    dados_membros = _get_dados_listar_membros(tipo_membro)

    return dados_membros

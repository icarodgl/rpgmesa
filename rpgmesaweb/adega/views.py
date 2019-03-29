import datetime

from django.forms import modelformset_factory
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from .models import Vendedor, Venda, Produto


def listar_vendedores(request):
    try:
        vendedores = Vendedor.objects.all()
    except Vendedor.DoesNotExist:
        raise Http404("Não existe")
    template = loader.get_template('adega/listar_vendedores.html')
    context = {
        'lista': vendedores,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    try:
        vendedores = Vendedor.objects.all()
    except Vendedor.DoesNotExist:
        raise Http404("Não existe")
    template = loader.get_template('adega/listar_vendedores.html')
    context = {
        'lista': vendedores,
    }
    return HttpResponse(template.render(context, request))

def Listar_vendas_periodo(request, mes,ano):
    try:
        vendas = Venda.objects.filter(data__year=ano, data__month=mes)
    except Venda.DoesNotExist:
        raise Http404("Não existe")
    template = loader.get_template('adega/listar_vendas.html')
    context = {
        'lista': vendas,
    }
    return HttpResponse(template.render(context, request))


def Listar_vendas_periodo_vendedor(request,vendedor_id,mes,ano):
    try:
        vendas = Venda.objects.filter(vendedor=vendedor_id,data__year=ano, data__month=mes)
    except Venda.DoesNotExist:
        raise Http404("Não existe")
    template = loader.get_template('adega/listar_vendas.html')
    context = {

        'lista': vendas,
    }
    return HttpResponse(template.render(context, request))


def nova_venda(request):
    vendaform = modelformset_factory(Venda, fields='__all__', extra=1)
    if request.method == "POST":
        formset = vendaform(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/adega/nova/venda')
    else:
        formset = vendaform()
    return render(request, 'adega/nova_venda.html', {'formset': formset})


def novo_produto(request):
    produtoform = modelformset_factory(Produto, fields='__all__', extra=1)
    if request.method == "POST":
        formset = produtoform(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/adega/novo/produto')
    else:
        formset = produtoform()
    return render(request, 'adega/nova_venda.html', {'formset': formset})


def editar_produto(request):
    pass

def editar_venda(request):
    pass

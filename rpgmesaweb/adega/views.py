import datetime

from django.forms import modelformset_factory, CheckboxSelectMultiple
from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from .models import Vendedor, Venda, Produto
from .form import VendaForm

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
        vendas = Venda.objects.filter(data__month=mes,data__year=ano)
    except Venda.DoesNotExist:
        raise Http404("Não existe")
    template = loader.get_template('adega/listar_vendas.html')
    context = {
        'lista': vendas,
    }
    return HttpResponse(template.render(context, request))

def Listar_vendas_todas(request):
    try:
        vendas = Venda.objects.all()
    except Venda.DoesNotExist:
        raise Http404("Não existe")
    template = loader.get_template('adega/listar_vendas.html')
    datas = []
    for i in vendas:

        data_dic = {'mes': i.data.strftime("%m"), 'ano': i.data.strftime("%y")}
        i.data = i.data.strftime("%d/%m/%Y")
        if data_dic not in datas:
            datas.append(data_dic)
    context = {
        'datas': datas,
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
    venda_form_set = modelformset_factory(model=Venda,can_delete=True, form=VendaForm)
    if request.method == "POST":
        formset = venda_form_set(request.POST, request.FILES,queryset=Venda.objects.filter(nome__startswith='0'))
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/adega/listar/vendas/todas/')
    else:
        formset = venda_form_set(queryset=Venda.objects.filter(nome__startswith='0'))

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

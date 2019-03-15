from django.http import HttpResponse
from .models import Pessoa
from django.template import loader
from django.http import Http404

def index(request):
    pessoas_list = Pessoa.objects.order_by('-criado')[:5]
    template = loader.get_template('usuarios/index.html')
    context = {
        'pessoas_list': pessoas_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, pessoa_id):
    try:
        pessoa = Pessoa.objects.get(pk=pessoa_id)
    except Pessoa.DoesNotExist:
        raise Http404("Pessoa Não existe")

    template = loader.get_template('usuarios/detalhe.html')
    context = {
        'pessoa': pessoa,
    }
    return HttpResponse(template.render(context, request))

def results(request, pessoa_id):
    response = "Você está buscando o usuario: %s."
    return HttpResponse(response % pessoa_id)

def vote(request, pessoa_id):
    return HttpResponse("Você está buscando o usuario: %s." % pessoa_id)
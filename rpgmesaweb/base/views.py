from django.template import loader, RequestContext
from django.http import Http404, HttpResponseRedirect,JsonResponse
from .models import Chave, Resposta
from django.views import generic
from django.http import HttpResponse
from django.forms import modelformset_factory, inlineformset_factory, formset_factory
from django.shortcuts import render, render_to_response
from .form import ChaveForm, RespostaForm

class IndexView(generic.ListView):

    def get_queryset(self):
        """Return the last five published questions."""
        return Chave.objects.order_by('-nome')


def index(request):
    lista = Chave.objects.order_by('-nome')
    template = loader.get_template('base/index.html')
    context = {
        'lista': lista,
    }
    return HttpResponse(template.render(context, request))


def detalhe(request, chave_id):
    try:
        chave = Chave.objects.get(pk=chave_id)
        resposta = Resposta.objects.filter(chave_id=chave_id)
        template = loader.get_template('base/detalhe.html')
    except Resposta.DoesNotExist:
        raise Http404("Não existe")
    
    context = {
        'chave': chave,
        'resposta': resposta,
    }
    return HttpResponse(template.render(context, request))
def detalhe_json(request, chave_id):
    try:
        chave = Chave.objects.get(pk=chave_id)
        resposta = Resposta.objects.filter(chave_id=chave_id)
    except Resposta.DoesNotExist:
        raise Http404("Não existe")

    str_chave = str(chave)
    context = {
        'chave': str_chave,
        'respostas': [],
    }
    for i in resposta:
        context['respostas'].append(i.resposta)
    return JsonResponse(context)
def resposta_chave_json(request, nome):
    try:
        chave = Chave.objects.get(nome=nome)
        resposta = Resposta.objects.filter(chave_id=chave.pk)
    except Resposta.DoesNotExist:
        raise Http404("Não existe")

    str_chave = str(chave)
    context = {
        'chave': str_chave,
        'respostas': [],
    }
    for i in resposta:
        context['respostas'].append(i.resposta)
    return JsonResponse(context)
def chaves_json(request):
    try:
        chave = Chave.objects.all()
    except Resposta.DoesNotExist:
        raise Http404("Não existe")

    chaves = []
    for i in chave:
        chaves.append(i.nome)
    return JsonResponse(chaves, safe=False)

def nova_chave(request):
    chaveForm = modelformset_factory(Chave, fields=("nome",))
    if request.method == "POST":
        formset = chaveForm(request.POST, request.FILES,
                            queryset=Chave.objects.filter(nome__startswith='0'))
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/chave/')
    else:
        formset = chaveForm(
            queryset=Chave.objects.filter(nome__startswith='0'))
    return render(request, 'base/novo.html', {'formset': formset})


def edit(request, pk):
    chave = Chave.objects.get(pk=pk)
    respostafs = inlineformset_factory(
        Chave, Resposta, form=RespostaForm, fields='__all__', extra=3)
    if request.method == ('POST' or None):
        formset = respostafs(request.POST, request.FILES, instance=chave)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/')
    else:
        formset = respostafs(instance=chave)

    return render(request, 'base/novo.html', {'formset': formset, })

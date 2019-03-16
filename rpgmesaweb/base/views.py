from django.template import loader
from django.http import Http404
from .models import Chave, Resposta
from django.views import generic
from django.http import HttpResponse


class IndexView(generic.ListView):

    def get_queryset(self):
        """Return the last five published questions."""
        return Chave.objects.order_by('-nome')


def index(request):
    lista = Chave.objects.order_by('-nome')[:5]
    template = loader.get_template('base/index.html')
    context = {
        'lista': lista,
    }
    return HttpResponse(template.render(context, request))


def detalhe(request, chave_id):
    try:
        chave = Chave.objects.get(pk=chave_id)
        resposta = Resposta.objects.filter(chave_id=chave_id)
    except Resposta.DoesNotExist:
        raise Http404("Não existe")

    template = loader.get_template('base/detalhe.html')
    context = {
        'chave': chave,
        'resposta': resposta,
    }
    return HttpResponse(template.render(context, request))

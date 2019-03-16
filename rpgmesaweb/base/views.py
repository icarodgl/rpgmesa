from django.template import loader
from django.http import JsonResponse

def index(request):
    data = [{"Mensagem":"Acordei"}]
    return JsonResponse(data,safe=False)

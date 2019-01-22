from django.shortcuts import render
from django.http import HttpResponse

from .models import Questionario, Pergunta, Alternativa


def index(request):
    questionarios = Questionario.objects.all()
    context = {'questionarios': questionarios}
    return render(request, 'questionario/index.html', context)

def detail(request, questionario_id):
    return HttpResponse("You're looking at question %s." % questionario_id)

def results(request, questionario_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionario_id)

def vote(request, questionario_id):
    return HttpResponse("You're voting on question %s." % questionario_id)
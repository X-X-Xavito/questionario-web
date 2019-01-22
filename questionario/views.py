from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Questionario, Pergunta, Alternativa


def index(request):
    questionarios = Questionario.objects.all()
    context = {'questionarios': questionarios}
    return render(request, 'questionario/index.html', context)

def detail(request, questionario_id):
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    context = {'questionario': questionario}
    return render(request, 'questionario/detail.html', context)

def results(request, questionario_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % questionario_id)

def vote(request, questionario_id):
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    #O for serve para iterar sobre cada pergunta recebido do POST.
    for pergunta_id in request.POST.getlist('pergunta'):
        try:
            alternativa_id = ''
            for chave_dict,valor_dict in request.POST.items():
                if chave_dict == pergunta_id:
                    alternativa_id = valor_dict
            pergunta = Pergunta.objects.get(pk=pergunta_id)
            alternativa_selecionada = Alternativa.objects.get(pk=alternativa_id)
        except (KeyError, Alternativa.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'questionario/detail.html', {
                'questionario': questionario,
                'error_message': "You didn't select a choice.",
            })
        else:
            alternativa_selecionada.votos += 1
            alternativa_selecionada.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
    return HttpResponseRedirect(reverse('questionario:results', args=(questionario.id,)))


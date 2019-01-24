"""
    Importa métodos de objetos do Django
    Importa as models dentro de models.py
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Questionario, Pergunta, Alternativa


def index(request):
    """
        Coleta todos os objetos Questionarios e retornar renderizados dentro de index.html
    """
    questionarios = Questionario.objects.all()
    context = {'questionarios': questionarios}
    return render(request, 'questionario/index.html', context)

def detalhes(request, questionario_id):
    """
        Coleta dentro dos objetos Questionario aquele com o questionario_id da URL. 
        Caso tenha, retornar renderizado dentro do detail.html
        Caso não tenha nenhum, exibir um erro 404.
    """
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    context = {'questionario': questionario}
    return render(request, 'questionario/detalhes.html', context)

def resultados(request, questionario_id):
    """
        Exibe a alternativa mais votada dentro dentro de cada pergunta e renderizar dentro de results.html
    """
    ganhadores={}
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    perguntas = Pergunta.objects.filter(questionario=questionario.id)
    for pergunta in perguntas:
        alternativas = Alternativa.objects.filter(pergunta=pergunta.id)
        ganhador = alternativas.order_by('-votos').first()
        ganhadores[pergunta] = ganhador
    context = {'questionario': questionario,
                'ganhadores': ganhadores, }
    return render(request, 'questionario/resultados.html', context)

def votar(request, questionario_id):
    """
        Recebe as informações do metodo POST do form em detail.html.
        Passar essas informações para o banco de dados e salvá-las
        A cada vez que o a função executar, irá adicionar ao atr contador do questionario.
        A função irá redirecionar para results.html
    """
    questionario = get_object_or_404(Questionario, pk=questionario_id)
    questionario.contador+=1
    questionario.save()
    for pergunta_id in request.POST.getlist('pergunta'):
        try:
            alternativa_id = ''
            for chave_dict,valor_dict in request.POST.items():
                if chave_dict == pergunta_id:
                    alternativa_id = valor_dict
            pergunta = Pergunta.objects.get(pk=pergunta_id)
            alternativa_selecionada = Alternativa.objects.get(pk=alternativa_id)
        except (KeyError, Alternativa.DoesNotExist):
            return render(request, 'questionario/detalhes.html', {
                'questionario': questionario,
                'error_message': "Vocẽ não selecionou uma alternativa.",
            })
        else:
            alternativa_selecionada.votos += 1
            alternativa_selecionada.save()
    return HttpResponseRedirect(reverse('questionario:resultados', args=(questionario.id,)))


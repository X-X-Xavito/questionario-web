from django.urls import path

from . import views

'''
    Arquivo que irá redirecionar as URLS recebidas.
    Cada path é uma url diferente. Para a URL 'vazia', por exemplo 'www.exemplo.com.br', irá verificar a view 'detail' para buscar novas instruções.
    A rota 'www.exemplo.com.br/5', irá verificar a view 'detail' para buscar novas instruções.
    A linha app_name é para separar as patterns para o app 'questionario' e para nenhuma outra.
'''

app_name = 'questionario'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questionario_id>/', views.detail, name='detail'),
    path('<int:questionario_id>/results/', views.results, name='results'),
    path('<int:questionario_id>/vote/', views.vote, name='vote'),
]

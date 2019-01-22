from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:questionario_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:questionario_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:questionario_id>/vote/', views.vote, name='vote'),
]

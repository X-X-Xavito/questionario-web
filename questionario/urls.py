from django.urls import path

from . import views

app_name = 'questionario'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questionario_id>/', views.detail, name='detail'),
    path('<int:questionario_id>/results/', views.results, name='results'),
    path('<int:questionario_id>/vote/', views.vote, name='vote'),
]

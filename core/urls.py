"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#Importar static, que é uma funçãoo auxiliar para retornar um padrão de URL para arquivos estáticos e de media.
from django.conf.urls.static import static
#Importar settings para acessar as configuração do Django
from django.conf import settings



urlpatterns = [
    #Incluido o path vazio para que o Django redirecionar as URLS recebidas para questionario.urls e procurar por instruções lá
    path('', include('questionario.urls')),
    path('admin/', admin.site.urls),
]
"""
    Inserção de movos elementos na lista 'urlpatterns', que irão indicar os padrões de URL dos arquivos estáticos e de 'medias'. 
    O Django irá olhar para o arquivo settings e procurar pelas URLS do STATIC e MEDIA e depois procurar a raiz do documento no caminho definido em ROOT dentro de settings.py
"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
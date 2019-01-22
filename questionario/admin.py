from django.contrib import admin

from .models import Questionario, Pergunta, Alternativa

# Register your models here.

admin.site.register(Questionario)
admin.site.register(Pergunta)
admin.site.register(Alternativa)


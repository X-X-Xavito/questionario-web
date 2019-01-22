from django.contrib import admin

from .models import Questionario, Pergunta, Alternativa

# Register your models here.
class QuestionarioAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields': ['titulo']}),
    ]


class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,             {'fields': ['texto']}),
    ('Imagem da Foto', {'fields': ['imagem']}),        
]
    list_filter = ('questionario',)
    list_display = ('texto','questionario',)


class AlternativaAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,             {'fields': ['texto']}),        
]
    list_filter = ('pergunta',)
    list_display = ('texto','pergunta',)


admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Alternativa, AlternativaAdmin)


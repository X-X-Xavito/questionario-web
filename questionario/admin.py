from django.contrib import admin

from .models import Questionario, Pergunta, Alternativa

# Register your models here.


class PerguntaInline(admin.TabularInline):
    model = Pergunta
    extra = 1
    max_num=10


class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2
    max_num = 4


class QuestionarioAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields': ['titulo']}),
    ]
    inlines = [PerguntaInline]

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,             {'fields': ['texto']}),
    ('Questionario Relacionado', {'fields': ['questionario']}),        
    ('Imagem da Foto', {'fields': ['imagem']}), 
]
    list_filter = ('questionario',)
    list_display = ('texto','questionario',)
    inlines = [AlternativaInline]


admin.site.register(Questionario, QuestionarioAdmin)
admin.site.register(Pergunta, PerguntaAdmin)



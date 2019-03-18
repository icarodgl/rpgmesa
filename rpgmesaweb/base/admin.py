from django.contrib import admin

from .models import Chave, Resposta


class RespostaInline(admin.StackedInline):
    model = Resposta
    extra = 1

class ChavenAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['nome']})
    ]
    inlines = [RespostaInline]


admin.site.register(Chave, ChavenAdmin)

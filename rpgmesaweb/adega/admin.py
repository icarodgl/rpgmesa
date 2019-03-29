from django.contrib import admin

from .models import Produto, Venda, Vendedor


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    pass

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    pass


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    pass

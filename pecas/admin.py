from django.contrib import admin

from .models import Peca


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ("nome", "fornecedor", "categoria", "preco", "estoque", "ativo")
    list_filter = ("categoria", "ativo")
    search_fields = ("nome",)
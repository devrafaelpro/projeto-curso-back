from django.shortcuts import render

from contas.decorators import comprador_required


def catalogo(request):
    return render(request, "em_breve.html", {"titulo": "Catálogo de peças"})


@comprador_required
def carrinho(request):
    return render(request, "em_breve.html", {"titulo": "Carrinho"})


@comprador_required
def meus(request):
    return render(request, "em_breve.html", {"titulo": "Meus pedidos"})
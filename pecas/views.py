from django.shortcuts import render

from contas.decorators import fornecedor_required


@fornecedor_required
def minhas(request):
    return render(request, "em_breve.html", {"titulo": "Minhas peças"})


@fornecedor_required
def nova(request):
    return render(request, "em_breve.html", {"titulo": "Cadastrar peça"})
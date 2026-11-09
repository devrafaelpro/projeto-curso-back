from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import CadastroForm


def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect("painel:inicio")
    else:
        form = CadastroForm()
    return render(request, "contas/cadastro.html", {"form": form})
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def inicio(request):
    user = request.user
    if user.is_superuser or user.tipo == "admin":
        return redirect("painel:admin")
    if user.tipo == "fornecedor":
        return redirect("painel:fornecedor")
    return redirect("painel:comprador")
from django.shortcuts import render

from contas.decorators import admin_required


@admin_required
def dashboard(request):
    return render(request, "painel/admin/dashboard.html")
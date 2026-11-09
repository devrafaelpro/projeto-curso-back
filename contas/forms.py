from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class CadastroForm(UserCreationForm):
    tipo = forms.ChoiceField(
        label="Quero me cadastrar como",
        choices=[
            (Usuario.Tipo.COMPRADOR, "Comprador"),
            (Usuario.Tipo.FORNECEDOR, "Fornecedor"),
        ],
    )

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("username", "first_name", "email", "tipo")
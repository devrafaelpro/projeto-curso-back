from django.conf import settings
from django.db import models


class Peca(models.Model):
    class Categoria(models.TextChoices):
        MOTOR = "motor", "Motor"
        FREIOS = "freios", "Freios"
        SUSPENSAO = "suspensao", "Suspensão"
        ELETRICA = "eletrica", "Elétrica"
        CARROCERIA = "carroceria", "Carroceria"
        OUTROS = "outros", "Outros"

    fornecedor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="pecas",
        limit_choices_to={"tipo": "fornecedor"},
    )
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    categoria = models.CharField(max_length=20, choices=Categoria.choices, default=Categoria.OUTROS)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(upload_to="pecas/", blank=True, null=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "peça"
        verbose_name_plural = "peças"

    def __str__(self):
        return self.nome
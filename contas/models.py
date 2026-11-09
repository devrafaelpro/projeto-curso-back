from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    class Tipo(models.TextChoices):
        COMPRADOR = "comprador", "Comprador"
        FORNECEDOR = "fornecedor", "Fornecedor"
        ADMIN = "admin", "Administrador"

    tipo = models.CharField(max_length=20, choices=Tipo.choices, default=Tipo.COMPRADOR)

    @property
    def is_fornecedor(self):
        return self.tipo == self.Tipo.FORNECEDOR

    @property
    def is_comprador(self):
        return self.tipo == self.Tipo.COMPRADOR
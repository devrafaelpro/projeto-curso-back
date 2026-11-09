from django.urls import path

from . import views

app_name = "pedidos"

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("carrinho/", views.carrinho, name="carrinho"),
    path("meus/", views.meus, name="meus"),
]
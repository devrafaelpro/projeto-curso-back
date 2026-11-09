from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(pattern_name="painel:inicio")),
    path("contas/", include("contas.urls")),
    path("pecas/", include("pecas.urls")),
    path("pedidos/", include("pedidos.urls")),
    path("painel/", include("painel.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
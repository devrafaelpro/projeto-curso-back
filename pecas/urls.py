from django.urls import path

from . import views

app_name = "pecas"

urlpatterns = [
    path("minhas/", views.minhas, name="minhas"),
    path("nova/", views.nova, name="nova"),
]
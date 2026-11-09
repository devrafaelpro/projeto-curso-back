from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("Perfil", {"fields": ("tipo",)}),)
    list_display = ("username", "email", "tipo", "is_active")
    list_filter = ("tipo", "is_active")
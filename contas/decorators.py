from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def tipo_required(*tipos):
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.is_superuser or user.tipo in tipos:
                return view(request, *args, **kwargs)
            raise PermissionDenied
        return wrapper
    return decorator


admin_required = tipo_required("admin")
fornecedor_required = tipo_required("fornecedor")
comprador_required = tipo_required("comprador")
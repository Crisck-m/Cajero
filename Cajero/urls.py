from django.contrib import admin
from django.urls import path, include
from operaciones.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),  # Redirigir la ruta raíz a la vista de inicio de sesión
    path('operaciones/', include('operaciones.urls')),  # Incluir las URLs de la aplicación operaciones
]

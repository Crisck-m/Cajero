from django.urls import path
from .views import login_view, register_view, home_view, depositar, retirar

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),  # Nueva ruta para el registro
    path('home/', home_view, name='home'),
    path('depositar/', depositar, name='depositar'),
    path('retirar/', retirar, name='retirar'),
]

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from .models import Cuenta

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Inicio de sesión exitoso para el usuario:", username)  # Mensaje de depuración
            return redirect('home')  # Redirigir a la nueva vista home_view
        else:
            print("Credenciales inválidas para el usuario:", username)  # Mensaje de depuración
            return render(request, 'operaciones/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'operaciones/login.html')

@login_required
def home_view(request):
    cuenta = Cuenta.objects.get(usuario=request.user.username)  # Obtener la cuenta del usuario
    saldo_total = cuenta.saldo  # Obtener el saldo total
    return render(request, 'operaciones/home.html', {'saldo': saldo_total})  # Renderizar la nueva página de inicio

@login_required
def depositar(request):
    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        cuenta = Cuenta.objects.get(usuario=request.user.username)
        cuenta.saldo += float(cantidad)  # Actualizar el saldo
        cuenta.save()
        return render(request, 'operaciones/depositar.html', {'mensaje': 'Depósito exitoso'})
    return render(request, 'operaciones/depositar.html')

@login_required
def retirar(request):
    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        cuenta = Cuenta.objects.get(usuario=request.user.username)
        if cuenta.saldo >= float(cantidad):
            cuenta.saldo -= float(cantidad)  # Actualizar el saldo
            cuenta.save()
            return render(request, 'operaciones/retirar.html', {'mensaje': 'Retiro exitoso'})
        else:
            return render(request, 'operaciones/retirar.html', {'mensaje': 'Saldo insuficiente'})
    return render(request, 'operaciones/retirar.html')

def register_view(request):
    User = get_user_model()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')  # Redirigir a la página de inicio de sesión después del registro
    return render(request, 'operaciones/register.html')

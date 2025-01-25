

from django.db import models

class Cuenta(models.Model):
    numero_cuenta = models.CharField(max_length=20, unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    usuario = models.CharField(max_length=100)
    def __str__(self):
        return self.numero_cuenta


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Auditoria(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    cambio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

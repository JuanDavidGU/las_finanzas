from django.db import models

# Create your models here.
class SalarioMinimos(models.Model):
    anio = models.PositiveIntegerField()
    salario_minimo = models.DecimalField(max_digits=10, decimal_places=(2))
    variacion = models.DecimalField(max_digits=10, decimal_places=(2))

    class Meta:
        verbose_name_plural = "Salarios Minimos"

    def __str__(self):
        return f'{self.salario_minimo}'
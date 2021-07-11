from django.db import models

# Create your models here.
class Edificio(models.Model):
    opciones_tipo_edificio = (
        ('residencial', 'residencial'),
        ('comercial', 'comercial'),
        )
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30, unique=True)
    tipo = models.CharField(max_length=30, \
            choices=opciones_tipo_edificio) 

    def __str__(self):
        return "%s %s %s %s" % (
                self.nombre, 
                self.direccion,
                self.ciudad,
                self.tipo)

    def obtener_total_cuartos(self):
        valor = [t.cuartos for t in self.departamentos.all()]
        valor = sum(valor)
        return valor

    def obtener_costo_total_departamentos(self):
        valor = [t.costoDept for t in self.departamentos.all()]
        valor = sum(valor)
        return valor

class Departamento(models.Model):
    nombPropietario = models.CharField(max_length=100)
    costoDept = models.DecimalField(max_digits=100, decimal_places=2)
    cuartos = models.IntegerField("Número de Cuartos")
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="departamentos")

    def __str__(self):
        return "%s %.2f %d %s" % (
            self.nombPropietario, 
            self.costoDept,
            self.cuartos,
            self.edificio
            )
from django.db import models


# Create your models here.
class Vehiculo(models.Model):
    marcas = [["Fiat", "Fiat"], ["Chevrolet", "Chevrolet"], ["Ford", "Ford"],
              [
                  "Toyota",
                  "Toyota",
              ]]
    marca = models.CharField(max_length=20, choices=marcas, default="Ford")
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categorias = [["Particular", "Particular"], ["Transporte", "Transporte"],
                  ["Carga", "Carga"]]
    categoria = models.CharField(max_length=20,
                                 choices=categorias,
                                 default="Particular")

    precio = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 blank=False,
                                 null=False)
    #auto_now_add Se añade una sola vez, cuando se crea el registro
    creacion = models.DateTimeField(auto_now_add=True)
    #auto_now Se modifica con cada cambio que se realize en el registro
    modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [("visualizar_catalogo", "Visualizar catalogos")]

    def condicion_precio(self):
        # Programo condiciones
        # Retornar valores en base a la condiciones
        if self.precio >= 0 and self.precio <= 10000:
            return "Bajo"
        elif self.precio >= 10001 and self.precio <= 30000:
            return "Medio"
        else:
            return "Alto"

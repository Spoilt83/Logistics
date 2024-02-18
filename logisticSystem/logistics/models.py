from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(verbose_name="Correo")
    phone = models.CharField(max_length=10, verbose_name="Teléfono")
    address = models.CharField(max_length=100, verbose_name="Dirección")

    def __str__(self):
        return f"{self.name} {self.last_name}"



class Transportist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido", null=True, blank=True)
    vihicle_type = models.CharField(max_length=100, verbose_name="Tipo de vehículo")
    contact_number = models.CharField(max_length=10, verbose_name="Teléfono de contacto")
    

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transportist = models.ForeignKey(Transportist, on_delete=models.CASCADE)
    weight = models.FloatField(verbose_name="Peso")
    dimensions = models.CharField(max_length=100, verbose_name="Dimensiones")
    origin = models.CharField(max_length=100, verbose_name="Origen")
    destination = models.CharField(max_length=100, verbose_name="Destino")
    status = models.CharField(max_length=100, verbose_name="Estado")

    def __str__(self):
        return f"{self.weight} {self.dimensions} {self.origin} {self.destination} {self.status} {self.client} {self.transportist}"
    



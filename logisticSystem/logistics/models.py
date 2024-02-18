from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.last_name}"



class Transportist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    vihicle_type = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=10)
    

    def __str__(self):
        return f"{self.name}"


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    transportist = models.ForeignKey(Transportist, on_delete=models.CASCADE)
    weight = models.FloatField()
    dimensions = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.status}"
    



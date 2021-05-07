from django.db import models

# Create your models here.
class Drivers (models.Model):
    name=models.CharField(max_length=400)
    age=models.CharField(max_length=400)
    email=models.EmailField(null=True ,blank=True)
    phonenumber=models.CharField(max_length=400)
    Type_of_car=models.CharField(max_length=400)
    carnumber=models.CharField(max_length=12)
    
    def __str__(self):
        return self.name

class Taxie(models.Model):
    status=[
        ('Available','Available'),
        ('Unavailable','Unavailable')
    ]
    The_beneficial_driver=models.ForeignKey(Drivers, on_delete=models.PROTECT, null=True, blank=True)
    status=models.CharField(max_length=50,choices=status,null=True, blank=True)
    client_name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=400)
    age_of_driver=models.IntegerField(null=True ,blank=True)
    location=models.CharField(max_length=400)
    To=models.CharField(max_length=400)
    def __str__(self):
        return self.client_name

class Buse (models.Model):
    status=[
        ('Available','Available'),
        ('Unavailable','Unavailable')
    ]
    The_beneficial_driver=models.ForeignKey(Drivers, on_delete=models.PROTECT, null=True, blank=True)
    status=models.CharField(max_length=50,choices=status,null=True, blank=True)
    client_name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=400)
    location=models.CharField(max_length=400)
    To=models.CharField(max_length=400)
    def __str__(self):
        return self.client_name

class Truckse(models.Model):
    status=[
        ('Available','Available'),
        ('Unavailable','Unavailable')
    ]
    The_beneficial_driver=models.ForeignKey(Drivers, on_delete=models.PROTECT, null=True, blank=True)
    status=models.CharField(max_length=50,choices=status,null=True, blank=True)
    client_name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=400)
    Type_of_load=models.CharField(max_length=400)
    location=models.CharField(max_length=400)
    To=models.CharField(max_length=400)
    def __str__(self):
        return self.client_name




from django.db import models

# Create your models here.
class Drivers (models.Model):
    name=models.CharField(max_length=400)
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
 
    choices_time=[
        ('8:00a.m','8:00a.m'),
        ('10:00a.m','10:00a.m'),
        ('12:00p.m','12:00p.m'),
        ('3:00p.m','3:00p.m'),
        ('8:00p.m','8:00p.m'),
        ('10:00p.m','10:00p.m'),
    ]
    The_beneficial_driver=models.ForeignKey(Drivers, on_delete=models.PROTECT, null=True, blank=True)
    status=models.CharField(max_length=50,choices=status,null=True, blank=True)
    client_name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=400)
    time=models.CharField(max_length=50,choices=choices_time,null=True, blank=True)
    location=models.CharField(max_length=400)
    To=models.CharField(max_length=400)
    def __str__(self):
        return self.client_name

class Buse (models.Model):
    status=[
        ('Available','Available'),
        ('Unavailable','Unavailable')
    ]

    choices_time=[
        ('8:00a.m','8:00a.m'),
        ('10:00a.m','10:00a.m'),
        ('12:00p.m','12:00p.m'),
        ('3:00p.m','3:00p.m'),
        ('8:00p.m','8:00p.m'),
        ('10:00p.m','10:00p.m'),
    ]
    The_beneficial_driver=models.ForeignKey(Drivers, on_delete=models.PROTECT, null=True, blank=True)
    status=models.CharField(max_length=50,choices=status,null=True, blank=True)
    client_name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=400)
    time=models.CharField(max_length=50,choices=choices_time,null=True, blank=True)
    location=models.CharField(max_length=400)
    To=models.CharField(max_length=400)
    def __str__(self):
        return self.client_name

class Truckse(models.Model):
    status=[
        ('Available','Available'),
        ('Unavailable','Unavailable')
    ]
  
    choices_time=[
        ('8:00a.m','8:00a.m'),
        ('10:00a.m','10:00a.m'),
        ('12:00p.m','12:00p.m'),
        ('3:00p.m','3:00p.m'),
        ('8:00p.m','8:00p.m'),
        ('10:00p.m','10:00p.m'),
    ]
    The_beneficial_driver=models.ForeignKey(Drivers, on_delete=models.PROTECT, null=True, blank=True)
    status=models.CharField(max_length=50,choices=status,null=True, blank=True)
    client_name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=400)
    time=models.CharField(max_length=50,choices=choices_time,null=True, blank=True)
    Type_of_load=models.CharField(max_length=400)
    location=models.CharField(max_length=400)
    To=models.CharField(max_length=400)
    def __str__(self):
        return self.client_name

##
class VipBuse (models.Model):
    status=[
        ('Available','Available'),
        ('Unavailable','Unavailable')
    ]
    choices_price=[
        ('80000','80000'),
        ('60000','60000'),
        ('According to the agreement','According to the agreement'),
       
    ]
    choices_time=[
        ('8:00a.m','8:00a.m'),
        ('10:00a.m','10:00a.m'),
        ('12:00p.m','12:00p.m'),
        ('3:00p.m','3:00p.m'),
        ('8:00p.m','8:00p.m'),
        ('10:00p.m','10:00p.m'),
    ]
    The_beneficial_driver=models.ForeignKey(Drivers, on_delete=models.PROTECT, null=True, blank=True)
    status=models.CharField(max_length=50,choices=status,null=True, blank=True)
    clientname=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=400)
    price=models.CharField(max_length=50,choices=choices_price,null=True, blank=True)
    time=models.CharField(max_length=50,choices=choices_time,null=True, blank=True)
    location=models.CharField(max_length=400)
    To=models.CharField(max_length=400)
    def __str__(self):
        return self.clientname

from django.db import models
from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name=models.CharField(max_length=50)
    year_founded=models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.name

class Phone(models.Model):

    phone_size=[
        ('SMALL','SMALL'),
        ('MEDIUM','MEDIUM'),
        ('LARGE','LARGE')
    ]

    model = models.CharField(max_length=50)
    manufacturer=models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    europe_in_out=models.BooleanField(default=False)
    size=models.CharField(max_length=10,choices=phone_size)
    new_phone=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    price=models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
        return self.model




# Create your models here.

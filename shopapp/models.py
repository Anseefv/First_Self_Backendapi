from django.db import models

# Create your models here.

class User(models.Model):

    username=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phone=models.PositiveBigIntegerField(unique=True,blank=True,null=True)
    age=models.PositiveIntegerField(blank=True,null=True)
    place=models.CharField(max_length=200,blank=True,null=True)

    role_options=[
        ('customer','customer'),
        ('seller','seller'),
        ('admin','admin'),
    ]
    role=models.CharField(max_length=20,choices=role_options ,default="customer")


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

    def __str__(self):
        return self.username

class Category(models.Model):

    name= models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):

    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
        on_delete=models.PROTECT,
        related_name='products',
        null=True,
        blank=True
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Store(models.Model):

    name=models.CharField(max_length=50,unique=True)
    description=models.TextField()
    seller=models.OneToOneField(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
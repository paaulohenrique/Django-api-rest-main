from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ManyToManyField(Client)
    products = models.ManyToManyField(Product)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.client.name}"

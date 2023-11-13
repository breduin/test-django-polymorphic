from django.db import models
from polymorphic.models import PolymorphicModel


class Product(PolymorphicModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} (product)'
    

class Service(Product):
    provider = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} (service)'


class Good(Product):
    manufacturer = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} (good)'


class PVS(Service):
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} (PVS)'


class OrderService(models.Model):
    number = models.PositiveIntegerField(
        blank=True,
        null=True,
        )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return f'{self.service.name} | {self.number}'


class OrderProduct(models.Model):
    number = models.PositiveIntegerField(
        blank=True,
        null=True,
        )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='orders',
        )

    def __str__(self):
        return f'{self.product.name} | {self.number}'

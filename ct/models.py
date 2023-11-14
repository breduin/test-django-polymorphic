# models.py
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from .utils import products_ids


class Service(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} (CT service)'

class Parking(Service):
    pass

    def __str__(self):
        return f'{self.name} (Parking)'


class Good(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} (good)'


class Order(models.Model):
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE,
        limit_choices_to={'pk__in': products_ids},
        )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        model = self.content_type
        obj = model.get_object_for_this_type(id=self.object_id)
        return f'Заказ {self.content_type} | {self.object_id} | {obj.name}'
# admin.py
from django.contrib import admin
from .models import Service, Parking, Good, Order

admin.site.register(Service)
admin.site.register(Parking)
admin.site.register(Good)
admin.site.register(Order)

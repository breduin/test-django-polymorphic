from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from .models import (
    Product,
    Service,
    Good,
    PVS,
    OrderProduct,
    OrderService,
    )


class ProductAdmin(PolymorphicParentModelAdmin):
    base_model = Product
    child_models = (Service, Good)


class ServiceAdmin(PolymorphicChildModelAdmin):
    base_model = Service


class GoodAdmin(PolymorphicChildModelAdmin):
    base_model = Good


class PVSAdmin(PolymorphicChildModelAdmin):
    base_model = PVS


class OrderProductAdmin(admin.ModelAdmin):
    base_model = OrderProduct


class OrderServiceAdmin(admin.ModelAdmin):
    base_model = OrderService


admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(PVS, PVSAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
admin.site.register(OrderService, OrderServiceAdmin)

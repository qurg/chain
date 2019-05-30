from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from company.models import Customer, Supplier


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(ModelAdmin):
    pass

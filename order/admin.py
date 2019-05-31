from django.contrib import admin
from django.contrib.admin import ModelAdmin


# Register your models here.
from order.models import TransOrder


@admin.register(TransOrder)
class TransOrderAdmin(ModelAdmin):
    pass
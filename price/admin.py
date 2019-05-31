from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from price.models import Inquire


@admin.register(Inquire)
class InquireAdmin(ModelAdmin):
    list_display = ['id', 'customer', 'destination']

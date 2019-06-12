from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from order.models import TransOrder


@admin.register(TransOrder)
class TransOrderAdmin(ImportExportModelAdmin):
    pass

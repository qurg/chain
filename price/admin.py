from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from price.models import Inquire, Quote


class QuoteAdmin(admin.StackedInline):
    model = Quote


@admin.register(Inquire)
class InquireAdmin(ModelAdmin):
    list_display = ['id', 'customer', 'depart', 'destination', 'carton', 'weight', 'volume']
    fieldsets = (
        (None, {'fields': (('customer', 'contact',),
                           ('depart', 'destination', 'cargo_ready'),
                           )}),
        ('货物信息', {'fields': (('carton', 'weight', 'volume',),
                             ('goods', 'airline_require',),
                             ('trans_time', 'remark',),
                             )}),
    )
    autocomplete_fields = ['customer', 'contact']
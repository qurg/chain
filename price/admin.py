import time

from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from price.adminForms import InquireForm, QuoteForm
from price.models import Inquire, Quote


class QuoteAdmin(admin.StackedInline):
    model = Quote
    form = QuoteForm
    fieldsets = (
        (None, {'fields': (('supplier',),
                           ('airline', 'airline_date'),
                           ('airline_remark', 'airline_times'),
                           ('weight_class', 'cost',),
                           ('net_rate', 'fuel_rate', 'security_rate', 'truck_rate',
                            'total_rate',),
                           ('dim', 'cut_share',),
                           ('trans_route', 'trans_time',),
                           'quote_remark',
                           )}),

    )

    autocomplete_fields = ['supplier', ]
    extra = 0


@admin.register(Inquire)
class InquireAdmin(ModelAdmin):
    form = InquireForm
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

    inlines = [QuoteAdmin, ]

    def save_model(self, request, obj, form, change):
        obj.create_by = request.user
        obj.created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return super(InquireAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        if formset.model != Quote:
            return super(InquireAdmin, self).save_formset(request, form, formset, change)

        instances = formset.save(commit=False)
        for instance in instances:
            instance.created_by = request.user
            instance.created = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            instance.save()
        formset.save_m2m()

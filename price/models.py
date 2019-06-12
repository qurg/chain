import time

from django.db import models
from company.models import Customer, Supplier
from django.conf import settings


# Create your models here.
class Price(models.Model):
    created = models.DateTimeField('创建时间')

    class Meta:
        abstract = True


class Inquire(Price):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, verbose_name='客户')
    destination = models.CharField('目的港', max_length=20)
    carton = models.IntegerField('件数')
    weight = models.FloatField('重量')
    volume = models.FloatField('体积')
    goods = models.CharField('品名', max_length=100)
    depart = models.CharField('始发港', max_length=20, default='TAO')
    cargo_ready = models.DateField('货好日期')
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                verbose_name='联系人', related_name='Inquire.contact+')
    airline_require = models.CharField('航司要求', max_length=300)
    trans_time = models.CharField('转运时间', max_length=200)
    remark = models.CharField('备注', max_length=500)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                  default=settings.AUTH_USER_MODEL, verbose_name='创建人')

    class Meta:
        verbose_name = '询价'
        verbose_name_plural = '询价管理'

    def __str__(self):
        return '客户: %s %s-%s 询价' % (self.customer, self.depart, self.destination)


class Quote(Price):
    airline = models.CharField('航空公司', max_length=100)
    airline_date = models.DateField('航班日期')
    airline_remark = models.CharField('航司说明', max_length=100)
    airline_times = models.CharField('航次', max_length=100)
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='供应商')
    weight_class = models.CharField('重量等级', max_length=100)
    cost = models.DecimalField('成本', max_digits=10, decimal_places=2)
    net_rate = models.DecimalField('单价', max_digits=10, decimal_places=2)
    fuel_rate = models.DecimalField('燃油', max_digits=10, decimal_places=2)
    security_rate = models.DecimalField('安全', max_digits=10, decimal_places=2)
    truck_rate = models.DecimalField('卡车单价', max_digits=10, decimal_places=2)
    total_rate = models.DecimalField('总计', max_digits=10, decimal_places=2)
    cut_share = models.CharField('切分泡', max_length=100)
    dim = models.CharField('密度', max_length=100)
    trans_route = models.CharField('路线', max_length=300)
    trans_time = models.CharField('转运时间', max_length=200)
    quote_remark = models.CharField('报价备注', max_length=500)
    inquire = models.ForeignKey(Inquire, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='询价')
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                  default=settings.AUTH_USER_MODEL, verbose_name='创建人')

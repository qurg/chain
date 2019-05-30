from django.db import models
from company.models import Customer, Supplier


# Create your models here.
class TransOrder(models.Model):
    num = models.CharField('订单号', max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='客户')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='供应商')

    def __str__(self):
        return self.num

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单管理'

from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField('公司名称', max_length=255)
    short_name = models.CharField('公司简称', max_length=255)

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name_plural = '合作伙伴'
        verbose_name = '合作伙伴'


class Customer(Company):
    pass

    class Meta:
        verbose_name = '客户'
        verbose_name_plural = '客户管理'


class Supplier(Company):
    account = models.CharField('银行账号', max_length=500)

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商管理'

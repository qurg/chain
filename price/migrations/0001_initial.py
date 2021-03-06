# Generated by Django 2.2.1 on 2019-06-12 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('destination', models.CharField(max_length=20, verbose_name='目的港')),
                ('carton', models.IntegerField(verbose_name='件数')),
                ('weight', models.FloatField(verbose_name='重量')),
                ('volume', models.FloatField(verbose_name='体积')),
                ('goods', models.CharField(max_length=100, verbose_name='品名')),
                ('depart', models.CharField(default='TAO', max_length=20, verbose_name='始发港')),
                ('cargo_ready', models.DateField(verbose_name='货好日期')),
                ('airline_require', models.CharField(max_length=300, verbose_name='航司要求')),
                ('trans_time', models.CharField(max_length=200, verbose_name='转运时间')),
                ('remark', models.CharField(max_length=500, verbose_name='备注')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Inquire.contact+', to=settings.AUTH_USER_MODEL, verbose_name='联系人')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Customer', verbose_name='客户')),
            ],
            options={
                'verbose_name': '询价',
                'verbose_name_plural': '询价管理',
            },
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(verbose_name='创建时间')),
                ('airline', models.CharField(max_length=100, verbose_name='航空公司')),
                ('airline_date', models.DateField(blank=True, null=True, verbose_name='航班日期')),
                ('airline_remark', models.CharField(blank=True, max_length=100, null=True, verbose_name='航司说明')),
                ('airline_times', models.CharField(blank=True, max_length=100, null=True, verbose_name='航次')),
                ('weight_class', models.CharField(blank=True, max_length=100, null=True, verbose_name='重量等级')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='成本')),
                ('net_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单价')),
                ('fuel_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='燃油')),
                ('security_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='安全')),
                ('truck_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='卡车单价')),
                ('total_rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总计')),
                ('cut_share', models.CharField(max_length=100, verbose_name='切分泡')),
                ('dim', models.CharField(max_length=100, verbose_name='密度')),
                ('trans_route', models.CharField(max_length=300, verbose_name='路线')),
                ('trans_time', models.CharField(max_length=200, verbose_name='转运时间')),
                ('quote_remark', models.CharField(blank=True, max_length=500, null=True, verbose_name='报价备注')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('inquire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='price.Inquire', verbose_name='询价')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.Supplier', verbose_name='供应商')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

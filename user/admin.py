from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from user.models import MyUser


admin.site.site_title = '供应链管理'
admin.site.site_header = '供应链管理'


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    pass

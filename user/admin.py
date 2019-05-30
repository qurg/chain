from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from user.models import MyUser


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    pass

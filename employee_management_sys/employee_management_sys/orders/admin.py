from django.contrib import admin

from employee_management_sys.orders.models import Order


# Register your models here.


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ("name","quantity",'is_done')
    list_filter = ('is_done',)

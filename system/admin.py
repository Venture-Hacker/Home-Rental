from django.contrib import admin
from .models import House, Order, PrivateMsg, Tenant, Owner
# Register your models here.

class HouseAdmin(admin.ModelAdmin):
    list_display = ("city", "image", "house_owner")
class OrderAdmin(admin.ModelAdmin):
    list_display = ("city", "from_date", "to", "tenant_name")

class PrivateMsgAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")

admin.site.register(House, HouseAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(PrivateMsg, PrivateMsgAdmin)
admin.site.register(Tenant)
admin.site.register(Owner)
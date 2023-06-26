from django.contrib import admin
from .models import Payment, ChargingPort

class ChargingPortAdmin(admin.ModelAdmin):
    list_display = ('port_number', 'is_available')

admin.site.register(ChargingPort, ChargingPortAdmin)
admin.site.register(Payment)

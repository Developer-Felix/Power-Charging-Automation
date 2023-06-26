from django.contrib import admin
from .models import Payment, ChargingPort

admin.site.register(Payment)
admin.site.register(ChargingPort)

from django.db import models

class ChargingPort(models.Model):
    port_number = models.IntegerField(unique=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Port {self.port_number}"


class Payment(models.Model):
    phone_number = models.CharField(max_length=15)
    access_code = models.CharField(max_length=4)
    minutes_paid = models.PositiveIntegerField(default=0)
    charging_port = models.OneToOneField(ChargingPort, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Payment for {self.phone_number}"

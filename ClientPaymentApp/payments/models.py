from django.db import models

class Payment(models.Model):
    phone_number = models.CharField(max_length=20)
    access_code = models.CharField(max_length=4)
    minutes_paid = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
    
 
class ChargingPort(models.Model):
    is_available = models.BooleanField(default=True)
    payment = models.OneToOneField('Payment', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Charging Port {self.id} - Available: {self.is_available}"

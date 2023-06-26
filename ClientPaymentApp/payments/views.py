from django.shortcuts import render
from django.http import JsonResponse

from .models import Payment
import random

def generate_access_code():
    access_code = random.randint(1000, 9999)
    return str(access_code)
def payment_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        minutes_paid = int(request.POST.get('minutes_paid'))

        # Perform payment processing here (e.g., using a payment gateway)

        # Generate random access code
        access_code = generate_access_code()

        # Save payment details
        payment = Payment.objects.create(phone_number=phone_number, access_code=access_code, minutes_paid=minutes_paid)

        # Return response to the client
        return JsonResponse({'success': True, 'access_code': access_code})

    return render(request, 'payment.html')


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Payment, ChargingPort

def charging_view(request):
    return render(request, 'charging.html')

def verify_access_code(request):
    if request.method == 'POST':
        access_code = request.POST.get('access_code')
        print(access_code)

        # Check if the access code exists and is valid
        payment = get_object_or_404(Payment, access_code=access_code)
        if payment.minutes_paid == 0:
            return JsonResponse({'success': False, 'message': 'Access code has already been used.'})

        # Find an available charging port
        charging_port = ChargingPort.objects.filter(is_available=True).first()
        if not charging_port:
            return JsonResponse({'success': False, 'message': 'No available charging ports.'})

        # Update the charging port and payment details
        charging_port.is_available = False
        charging_port.payment = payment
        charging_port.save()

        payment.minutes_paid -= 1
        payment.save()
        return render(request, 'charging.html')
    return render(request, 'charging.html')
   
    #     return JsonResponse({'success': True, 'message': 'Charging started successfully.'})

    # return JsonResponse({'success': False, 'message': 'Invalid request.'})


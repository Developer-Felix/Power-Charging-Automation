from django.urls import path

from . import views

urlpatterns = [
    path('payment/', views.payment_view, name='payment'),path('charge/', views.verify_access_code, name='charge'),
]

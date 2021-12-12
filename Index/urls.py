from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('payment-status' , views.payment_status , name='payment_status'),
    path('live' , views.live , name='live')
]

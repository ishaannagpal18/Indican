from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('payment-status' , views.payment_status , name='payment_status'),
    path('lobby' , views.lobby , name='lobby'),
    path('exhibition' , views.exhibition , name='exhibition'),
    path('auditorium' , views.auditorium , name='auditorium'),
    path('ninja' , views.ninja , name='ninja'),
    path('tic-tac-toe' , views.tic_tac_toe , name='tic-tac-toe'),
    path('planet_defense' , views.planet_defense , name='planet_defense'),
    path('snake' , views.snake , name='snake'),
    path('selfie' , views.selfie , name='selfie'),
]

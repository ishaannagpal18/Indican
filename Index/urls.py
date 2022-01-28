from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('demo',views.demo,name='demo'),
    path('demo1',views.demo1,name='demo1'),
    path('launch',views.launch,name='launch'),
    path('aboutus' , views.aboutus , name='aboutus'),
    path('brochure' , views.brochure , name='brochure'),
    path('membership' , views.membership , name='membership'),
    path('payment-status' , views.payment_status , name='payment_status'),
    path('l@123' , views.lobby , name='lobby'),
    path('e@123' , views.exhibition , name='exhibition'),
    path('a@123' , views.auditorium , name='auditorium'),
    path('c@123' , views.clubhouse , name='clubhouse'),
    path('n@123' , views.ninja , name='ninja'),
    path('t@123' , views.tic_tac_toe , name='tic-tac-toe'),
    path('p@123' , views.planet_defense , name='planet_defense'),
    path('s@123' , views.snake , name='snake'),
    path('se@123' , views.selfie , name='selfie'),
    path('d@123' , views.details , name='details'),
]

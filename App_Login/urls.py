from django.urls import path
from App_Login import views
from django.contrib.auth import views as auth_views

app_name = 'App_Login'

urlpatterns=[
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('subscriber_payment/',views.subscriber_payment,name='subscriber_payment'),
    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)



]

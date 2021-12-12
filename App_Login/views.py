from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash

from App_Login.models import UserProfile, Subscriber
from App_Login.forms import ProfileForm, SignUpForm, UserProfileChange, SubscriberForm

from django.contrib import messages
import razorpay

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/sign_up.html', context={'form':form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_Login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"You Are Logged Out!")
    return HttpResponseRedirect(reverse('home'))

@login_required
def change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            return HttpResponseRedirect(reverse('App_Login:login'))
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'App_Login/change-password.html', {'form':fm})

@login_required(login_url='/account/login')
def subscriber_payment(request):
    if request.method == 'POST':
        subs = request.user;
        amount = 500000;
        client = razorpay.Client(auth=('rzp_test_uxpXt2M6OCK6fN','UgT5LV4PMBIS6JBV5nLcLBcu'))

        response_payment = client.order.create(dict(amount=amount, currency='INR'))
        order_id = response_payment['id']
        order_status = response_payment['status']
        if order_status == 'created':
            subscriber = Subscriber(
                subs = subs,
                order_id = order_id
            )
            subscriber.save()
            response_payment['name']: request.user
            form = SubscriberForm(request.POST or None)
            return render(request, 'App_Login/subscriber_payment.html', {'form':form, 'payment':response_payment})
    form = SubscriberForm()
    return render(request, 'App_Login/subscriber_payment.html', {'form':form})

from django.http import HttpResponse
from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from App_Login.models import UserProfile, Subscriber

def home(request):
    return render(request, 'index.html')


def payment_status(request):
    response = request.POST
    print(response)

    params_dict = {
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    client = razorpay.Client(auth=('rzp_test_uxpXt2M6OCK6fN','UgT5LV4PMBIS6JBV5nLcLBcu'))
    try:
        status = client.utility.verify_payment_signature(params_dict)
        print(status)
        subscriber = Subscriber.objects.get(order_id=response['razorpay_order_id'])
        subscriber.razorpay_payment_id = response['razorpay_payment_id']
        subscriber.paid = True
        subscriber.save()
        return render(request, "payment_status.html", {'status': True})
    except:
        return render(request, "payment_status.html", {'status': False})



@login_required(login_url='/account/login')
def auditorium(request):
    return render(request, "auditorium.html")

@login_required(login_url='/account/login')
def lobby(request):
    return render(request, 'lobby.html')

@login_required(login_url='/account/login')
def exhibition(request):
    return render(request, 'exhibition.html')

@login_required(login_url='/account/login')
def ninja(request):
    return render(request, 'ninja.html')

@login_required(login_url='/account/login')
def tic_tac_toe(request):
    return render(request, 'tic-tac-toe.html')

@login_required(login_url='/account/login')
def planet_defense(request):
    return render(request, 'planet_defense.html')

@login_required(login_url='/account/login')
def snake(request):
    return render(request, 'snake.html')

@login_required(login_url='/account/login')
def selfie(request):
    return render(request, 'selfie.html')

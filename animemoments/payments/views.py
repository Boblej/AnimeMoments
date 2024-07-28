import uuid
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from yookassa import Configuration, Payment
from config.paymentconfig import SHOPID, KEY
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PaymentStatus

Configuration.account_id = SHOPID
Configuration.secret_key = KEY


def create_payment(price, title, meta):
    payment_id = str(uuid.uuid4())

    payment = Payment.create({
        "amount": {
            "value": price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "http://127.0.0.1:8000/payment_complete"
        },
        "capture": True,
        "description": title,
        "metadata": meta
    }, payment_id)

    return payment


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            payment_id = request.POST.get('object', {}).get('id')
            payment = Payment.find_one(payment_id)

            if payment.status == 'succeeded':
                user_id = payment.metadata.get('user_id')
                user = get_object_or_404(User, id=user_id)

                payment_status, created = PaymentStatus.objects.get_or_create(user=user)
                payment_status.is_payment_complete = True
                payment_status.save()

            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(status=500)
    else:
        return HttpResponse(status=404)


@login_required
def payment_complete(request):
    payment_status = get_object_or_404(PaymentStatus, user=request.user)

    if not payment_status.is_payment_complete:
        return redirect('land')

    payment_status.is_payment_complete = False
    payment_status.save()

    data = {
        'title': 'Payment Complete'
    }
    return render(request, 'payment/payment_complete.html', data)

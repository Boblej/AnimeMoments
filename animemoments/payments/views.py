import json
import uuid
from datetime import timedelta
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from yookassa import Configuration, Payment
from config.paymentconfig import SHOPID, KEY
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PaymentStatus
from subscription.models import Subscription

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
            "return_url": "https://59bf-190-2-133-175.ngrok-free.app/subscription"
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
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        payment_object = payload.get('object', {})

        if payment_object.get('status') == 'succeeded':
            user_id = int(payment_object['metadata'].get('user_id'))
            user = get_object_or_404(User, id=user_id)

            payment_status, created = PaymentStatus.objects.get_or_create(user=user)
            payment_status.is_payment_complete = True
            payment_status.save()

            subscription, created = Subscription.objects.get_or_create(user=user)
            subscription_type = payment_object['metadata'].get('subscription_type')
            subscription.is_active = True
            subscription.subscription_type = subscription_type

            if subscription.subscription_type == 'monthly':
                subscription.end_date = datetime.datetime.now() + timedelta(days=30)
            elif subscription.subscription_type == 'semi_annual':
                subscription.end_date = datetime.datetime.now() + timedelta(days=182)
            elif subscription.subscription_type == 'annual':
                subscription.end_date = datetime.datetime.now() + timedelta(days=365)

            subscription.save()

        return HttpResponse(status=200)

    else:
        return HttpResponse(status=404)

@login_required
def payment_complete(request):
    try:
        payment_status = PaymentStatus.objects.get(user=request.user)
    except PaymentStatus.DoesNotExist:
        return redirect('land')

    if not payment_status.is_payment_complete:
        return redirect('land')

    payment_status.is_payment_complete = False
    payment_status.save()

    return render(request, 'payment/payment_complete.html')
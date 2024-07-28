from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from payments.views import create_payment
from .models import Subscription
from .forms import SubscriptionForm
from django.utils import timezone
from datetime import timedelta


@login_required
def Subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():

            subscription_type = form.cleaned_data['subscription_type']
            price = '500.00' if subscription_type == 'monthly' else (
            '2400.00' if subscription_type == 'semi_annual' else '4300.00')
            meta = {'user_id': request.user.id, 'subscription_type': subscription_type}

            payment = create_payment(price, 'Subscription', meta)

            return redirect(payment.confirmation.confirmation_url)
    else:
        form = SubscriptionForm()

    return render(request, 'subscription/Subscription.html', {'form': form})


@login_required
def payment_complete(request):
    subscription = get_object_or_404(Subscription, user=request.user)

    if not subscription.is_active:
        subscription.is_active = True
        if subscription.subscription_type == 'monthly':
            subscription.end_date = timezone.now() + timedelta(days=30)
        elif subscription.subscription_type == 'semi_annual':
            subscription.end_date = timezone.now() + timedelta(days=182)
        elif subscription.subscription_type == 'annual':
            subscription.end_date = timezone.now() + timedelta(days=365)
        subscription.save()

    return render(request, 'subscription/payment_complete.html', {'title': 'Подписка активирована'})

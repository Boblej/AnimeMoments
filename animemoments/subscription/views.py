from django.shortcuts import render, redirect
from payments.views import create_payment
from .models import Subscription
from .forms import SubscriptionForm


def Subscription(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid() and request.COOKIES.get('login_success'):

            subscription_type = form.cleaned_data['subscription_type']
            price = '500.00' if subscription_type == 'monthly' else (
                '2400.00' if subscription_type == 'semi_annual' else '4300.00')
            meta = {'user_id': request.user.id, 'subscription_type': subscription_type}

            payment = create_payment(price, 'Subscription', meta)

            return redirect(payment.confirmation.confirmation_url)

        else:
            return redirect('register')

    else:
        form = SubscriptionForm()

    return render(request, 'subscription/Subscription.html', {'form': form})


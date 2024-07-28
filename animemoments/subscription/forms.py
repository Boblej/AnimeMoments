from django import forms

class SubscriptionForm(forms.Form):
    subscription_type = forms.CharField(widget=forms.HiddenInput())

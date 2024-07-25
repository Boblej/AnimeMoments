from django.shortcuts import render
from django.views.generic import TemplateView

class Subscription(TemplateView):
    template_name = 'subscription/Subscription.html'
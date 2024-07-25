from django.shortcuts import render
from django.views.generic import TemplateView

class Social(TemplateView):
    template_name = 'social/social.html'
from django.shortcuts import render
from django.views.generic import TemplateView

class Land(TemplateView):
    template_name = 'land/land.html'
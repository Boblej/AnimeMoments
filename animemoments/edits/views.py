from django.shortcuts import render
from django.views.generic import TemplateView

class Edits(TemplateView):
    template_name = 'edits/edits.html'
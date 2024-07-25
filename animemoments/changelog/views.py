from django.shortcuts import render
from django.views.generic import TemplateView

class Changelog(TemplateView):
    template_name = 'changelog/changelog.html'
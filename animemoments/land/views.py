from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class Land(TemplateView):
    template_name = 'land/land.html'

    def is_active_cookie(self, request, *args, **kwargs):
        if request.COOKIES.get('login_success'):
            return redirect('clips')
        return super().get(request, *args, **kwargs)
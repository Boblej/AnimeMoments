from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import RegistrationUser, LoginUser, UserChangePass

class RegisterUser(CreateView):
    form_class = RegistrationUser
    template_name = 'user/register.html'
    extra_context = {'title': 'Регистрация пользователя'}
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie('registration_success', 'true', max_age=86400)
        return response

class LoginUserView(LoginView):
    form_class = LoginUser
    template_name = 'user/login.html'
    extra_context = {'title': 'Login'}

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.COOKIES.get('registration_success'):
            response.delete_cookie('registration_success')
            return redirect('clips')
        return response

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('land'))

class UserPassChange(PasswordChangeView):
    form_class = UserChangePass
    success_url = reverse_lazy('users:login')
    template_name = 'user/forgot_pass.html'
    extra_context = {'title': 'Forgot Password'}

@login_required
def Clips(request):
    return render(request, 'user/Clips.html', {'title': 'AnimeMoments'})
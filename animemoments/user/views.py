from django.contrib.auth import logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegistrationUser, LoginUser, UserChangePass, AvatarForm
from .models import Profile

class RegisterUser(CreateView):
    form_class = RegistrationUser
    template_name = 'user/register.html'
    extra_context = {'title': 'Регистрация пользователя'}
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class LoginUserView(LoginView):
    form_class = LoginUser
    template_name = 'user/login.html'
    extra_context = {'title': 'Login'}

    def form_valid(self, form):
        response = super().form_valid(form)
        response.set_cookie('login_success', 'true', max_age=60*60*24*7)
        if self.request.COOKIES.get('login_success'):
            return redirect('land')
        return response

def logout_user(request):
    response = HttpResponseRedirect(reverse('land'))
    response.delete_cookie('login_success')
    logout(request)
    return response

class UserPassChange(PasswordChangeView):
    form_class = UserChangePass
    success_url = reverse_lazy('login')
    template_name = 'user/forgot_pass.html'
    extra_context = {'title': 'Forgot Password'}


@login_required
def profile_view(request):
    profile = get_object_or_404(User, id=request.user.id)

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user_profile = get_object_or_404(Profile, user_id=request.user.id)
                user_profile.delete()
            except:
                pass
            avatar_form = form.save(commit=False)
            avatar_form.user = profile
            avatar_form.save()
            return redirect('profile')

    user_profile = None
    try:
        user_profile = get_object_or_404(Profile, user_id=request.user.id)
    except:
        pass
    form = AvatarForm(instance=profile)
    return render(request, 'user/profile.html', {'form': form, 'user_profile': user_profile})




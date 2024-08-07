from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .models import Profile

class RegistrationUser(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'input-form', 'placeholder': 'Username'})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class':'input-form', 'placeholder': 'Email'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input-form', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input-form', 'placeholder': 'Confirm Password'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()

        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already registered.')

        return email

class LoginUser(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-form', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'input-form', 'placeholder': 'Password'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class UserChangePass(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': _('Current Password')})
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': _('New Password')}),
        help_text=_("Your password must contain at least 8 characters.")
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': _('Confirm New Password')})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']
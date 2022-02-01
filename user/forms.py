from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input input--text',
            'placeholder': 'Enter your Username...'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input input--password',
            'placeholder': '*******'
        }
    ))

class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input--text', 'autofocus': 'autofocus'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input--text', 'autofocus': ''}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input input--text', 'autofocus': ''}))
    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(attrs={'class': 'input input--email', 'autofocus': ''}))
    avatar = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'input input--file', 'autofocus': ''}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input input--password', 'autofocus': ''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input input--password', 'autofocus': ''}))
    is_admin = forms.BooleanField()
    is_staff = forms.BooleanField()
    class Meta:
        model = Profile
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'avatar',
            'password1',
            'password2',
            'is_admin',
            'is_staff'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

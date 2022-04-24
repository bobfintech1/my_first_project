from django import forms
from django.contrib.auth import authenticate

from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Bro oqip ciqip toldirarsiz ')

    class Meta:
        model = Account
        fields = ['email', 'phone_number', 'password1']


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('invalid inputs')


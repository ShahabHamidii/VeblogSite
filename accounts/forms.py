from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms import ValidationError



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Enter your username...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Enter your password...'}))

    def clean(self):
        user = authenticate(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
        if not user:
            raise ValidationError("Invalid username or password")


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email' ]
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Edit your first name...'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Edit your last name...'}),
                   'email' : forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Edit your email...'}),
        }

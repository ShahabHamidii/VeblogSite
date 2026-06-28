from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter your message...'}),
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your name...' }),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email...'}),
        }

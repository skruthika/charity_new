from django import forms
from .models import signup

class SignupForm(forms.ModelForm):
    class Meta:
        model = signup
        fields = ['fullname', 'email', 'password', 'confirm_password']

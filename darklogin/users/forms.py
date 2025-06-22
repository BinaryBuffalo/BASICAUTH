from django import forms
from captcha.fields import CaptchaField

class MyForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    captcha = CaptchaField(error_messages={'invalid': 'INVALID'})

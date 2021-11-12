from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat password')

    class Meta:
        model = User
        fields = ['username']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match! ')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if cd['username'] == 'Umar':
            raise forms.ValidationError('This user name is un usable')
        return cd['username']

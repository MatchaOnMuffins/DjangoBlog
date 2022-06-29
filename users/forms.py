from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import My_mode


class My_form1(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class Img_form(forms.ModelForm):
    class Meta:
        model = My_mode
        fields = "__all__"

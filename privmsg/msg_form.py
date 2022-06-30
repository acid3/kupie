from django import forms
from django.contrib.auth.models import User
from .models import prvMsg


class UserForm(forms.ModelForm):
    class Meta():
        model = prvMsg
        # model = User
        fields = ['reciver_id', 'msg']

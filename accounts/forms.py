from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'password', 'is_staff']

        widgets = {
            # telling Django your password field in the mode is a password input on the template
            'password': forms.PasswordInput()
        }

        # def save(self, commit=True):
        #     user = super(UserForm, self).save(commit=False)
        #     user.set_password(self.cleaned_data["password"])
        #     # if commit:
        #     user.save()
        #     return user

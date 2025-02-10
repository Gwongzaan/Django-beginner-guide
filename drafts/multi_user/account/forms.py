from django import forms
from django.contrib.auth.models import User

from .models import UserInfo, UserProfile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ("username", "email")

    def clearn_passwords(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("passwords do not match")
        return cd["password2"]


class userProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "phone",
            "birth",
        )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = (
            "school",
            "photo",
        )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email",)

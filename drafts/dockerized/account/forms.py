# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

from django import forms
from django.contrib.auth.models import User
from account.models import UserInfo, userProfile

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email')


    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=userProfile
        fields = ('phone', 'birth')


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme', 'photo')
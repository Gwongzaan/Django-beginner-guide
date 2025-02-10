from celery.worker.control import reserved
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.reverse import reverse

from account import forms
# Create your views here.

def user_login(request):
    if request.method == 'GET':
        login_form = forms.LoginForm()
        return render(request, template_name='account/login.html', context={'form': login_form})
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Login Successful')
            else:
                return HttpResponse('Login Failed')
        else:
            return HttpResponse('invalid login')

def register(request):
    if request.method == 'GET':
        return render(request,
                      template_name='account/register.html',
                      context={
                          'form': forms.RegisterForm(),
                          'profile': forms.UserProfileForm(),
                      })
    if request.method == 'POST':
        user_form = forms.RegisterForm(request.POST)
        user_profile_form = forms.UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = user_profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            # return HttpResponse('successful')
            return HttpResponseRedirect(reverse('account:login'))

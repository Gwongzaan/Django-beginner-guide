from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm, RegistrationForm, UserForm, UserInfoForm, userProfileForm
from .models import UserInfo, UserProfile

# Create your views here.


def user_login(request):
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            user = authenticate(
                username=cleaned_data["username"], password=cleaned_data["password"]
            )
            if user:
                login(request, user)
                return HttpResponse("Welocome")

            else:
                return HttpResponse("username or password is not right")

        else:
            return HttpResponse("Invalid login")


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        user_profile_form = userProfileForm(request.POST)
        if user_form.is_valid() and user_profile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = new_user
            user_profile.save()
            return HttpResponse("register successfully")

        else:
            return HttpResponse("failed to register")
    else:
        user_form = RegistrationForm()
        user_profile_form = userProfileForm()
        return render(
            request,
            "account/register.html",
            {"form": user_form, "profile": user_profile_form},
        )


@login_required()
def personal_info(request):
    user_profile = (
        UserProfile.objects.get(user=request.user)
        if hasattr(request.user, "userprofile")
        else UserProfile.objects.create(user=request.user)
    )
    user_info = (
        UserInfo.objects.get(user=request.user)
        if hasattr(request.user, "userinfo")
        else UserInfo.objects.create(user=request.user)
    )
    return render(
        request,
        "account/personal_info.html",
        {"user": request.user, "user_info": user_info, "user_profile": user_profile},
    )


@login_required()
def edit_info(request):
    user_profile = (
        UserProfile.objects.get(user=request.user)
        if hasattr(request.user, "userprofile")
        else UserProfile.objects.create(user=request.user)
    )
    user_info = (
        UserInfo.objects.get(user=request.user)
        if hasattr(request.user, "userinfo")
        else UserInfo.objects.create(user=request.user)
    )

    if request.method == "POST":
        user_form = UserForm(request.POST)
        user_profile_form = userProfileForm(request.POST)
        user_info_form = UserInfoForm(request.POST)

        if (
            user_form.is_valid()
            and user_profile_form.is_valid()
            and user_info_form.is_valid()
        ):
            user_cd = user_form.cleaned_data
            user_profile_cd = user_profile_form.cleaned_data
            user_info_cd = user_info_form.cleaned_data
            request.user.email = user_cd["email"]
            user_info.school = user_info_cd["school"]
            user_profile.birth = user_profile_cd["birth"]
            user_profile.phone = user_profile_cd["phone"]
            request.user.save()
            user_profile.save()
            user_info.save()

        return HttpResponseRedirect("/account/info/")

    else:
        user_form = UserForm(instance=request.user)
        user_profile_form = userProfileForm(
            initial={"birth": user_profile.birth, "phone": user_profile.phone}
        )
        user_info_form = UserInfoForm(initial={"school": user_info.school})

        return render(
            request,
            "account/edit_info.html",
            {
                "user_form": user_form,
                "userprofile_form": user_profile_form,
                "userinfo_form": user_info_form,
            },
        )


@login_required()
def user_image(request):
    if request.method == "POST":
        img = request.POST["img"]
        user_info = UserInfo.objects.get(user=request.user.id)
        user_info.photo = img
        user_info.save()
        return HttpResponse("1")
    else:
        return render(request, "account/imagecrop.html")

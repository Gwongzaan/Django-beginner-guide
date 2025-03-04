from account import views
from django.contrib.auth import views as auth_views
from django.urls import path, reverse

urlpatterns = [
    # path("login/", views.user_login, name="user_login"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="account/login2.html"),
        name="user_login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="account/logout.html"),
        name="user_logout",
    ),
    path("register/", views.register, name="user_register"),
    path(
        "password-change-done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="account/password_change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="account/password_change_form.html",
            # success_url=reverse("account:password_change_done"),
            success_url="/account/password-change-done/",
        ),
        name="password_change",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset_form.html",
            email_template_name="account/password_reset_email.html",
            success_url="/account/password-reset-done/",
        ),
        name="passwrod_reset",
    ),
    path(
        "password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_confirm.html",
            success_url="/account/password-reset-complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("info", views.personal_info, name="personal_info"),
    path("edit_info", views.edit_info, name="edit_info"),
    path("my-image/", views.user_image, name="user_image"),
]

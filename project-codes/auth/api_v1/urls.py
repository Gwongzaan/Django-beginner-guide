from django.urls import path
from .verification import VerificationCodeView 
from .registration import RegisterView
urlpatterns = [
    path('vcode/', VerificationCodeView.as_view(), name='verification_code'),
    path('register/', RegisterView.as_view(), name='register' ),
]

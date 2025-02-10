from rest_framework.views import APIView
from django.http.response import HttpResponse
from ugc.models import VerificationCode
from users.models import UserProfile
import json
import datetime

class RegisterView(APIView):
    def get(self,request):
        username=request.GET.get('username')
        pwd=request.GET.get('pwd')
        phone=request.GET.get('phone')
        email=request.GET.get('email')
        code=request.GET.get('code')
        if username:
            pass
        else:
            msg = 'enter username！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
            content_type="application/json,charset=utf-8")
        if pwd:
            pass
        else:
            msg = 'enter password！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
            content_type="application/json,charset=utf-8")
        if phone:
            pass
        else:
            msg = 'enter phone number！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
            content_type="application/json,charset=utf-8")
        if email:
            pass
        else:
            msg = 'enter email！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
            content_type="application/json,charset=utf-8")
        if code:
            pass
        else:
            msg = 'enter verification code！'
            result = {"status": "404", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
            content_type="application/json,charset=utf-8")
        code1=VerificationCode.objects.filter(phone=phone).last()
        if code==code1:
            end_time=code1.end_time
            end_time=end_time.replace(tzinfo=None)
            if end_time > datetime.datetime.now():
                user = UserProfile()
                user.username = username
                user.password = pwd
                user.phone = phone
                user.email=email
                user.save()
                msg = 'register successfully'
                result = {"status": "200", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                content_type="application/json,charset=utf-8")
            else:
                msg = 'verification code expired！'
                result = {"status": "403", "data": {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                content_type="application/json,charset=utf-8")
        else:
            msg = 'wrong verification code！'
            result = {"status": "403", "data": {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
            content_type="application/json,charset=utf-8")

class ActivationEmailView(APIView):
    def get(self, request):
        email = request.GET.get('email')
        if email:
            pass
        else:
            pass

class ActivetionView(APIView):
    def get(self, request):
        pass
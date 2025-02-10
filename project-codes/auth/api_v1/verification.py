from django.http.response import HttpResponse
from rest_framework.views import APIView
from users.models import UserProfile
from ugc.models import VerificationCode
from util.messages import Messager
import datetime
import json
import random

class VerificationCodeView(APIView):

    def get(self, request):
        '''
        if phone format valid
        if hpone number registered
        if validation code sent
        if validation expired
        generate verification code
        set expiration
        send verification code
        '''
        phone = request.GET.get('phone')

        if phone == '':
            msg = "please provide phone number"
            result = {'status': '444', 'data': {'msg': msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')

        
        if Messager.is_valid_phone_format(phone):
            # if phone number is registered
            if UserProfile.objects.filter(phone=phone):
                msg = "Phone number is registered"
                result = {'status': '402', 'data': {'msg': msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')
            # if verification code sent
            last_code = VerificationCode.objects.filter(phone=phone).last() 
            if last_code.add_time.replace(tzinfo=None) > datetime.datetime.now() - datetime.timedelta(minutes=1):
                msg = ""
                result = {'status': '403', 'data': {'msg':msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')
            else:
                code = VerificationCode()
                code.phone = phone
                c = random.randint(10000, 99999)
                code.code = str(c)
                code.end_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
                code.save()
                res = Messager.send_sms(phone, f"your verification code: {code.code}")

                if res:
                    msg = ''

                result = {'status': '200', 'data': {'msg':msg}}
                return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')
        else:
            msg = 'Invalid phone format'
            result = {'status': '405', 'msg': msg}
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json,charset=utf-8')


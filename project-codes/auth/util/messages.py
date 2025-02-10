from twilio.rest import Client
from django.conf import settings
import re

class Messager:
    def __init__(self):
        self.client = Client(settings.MSG_ACCT, settings.MSG_TOKEN)

    def send_sms(self, body, mobile_num):
        if self.is_phone_valid(mobile_num=mobile_num):
            self.client.messages.create(to=mobile_num, from_=settings.MSG_FROM, body=body) 

    def is_phone_valid(self, mobile_num):
        phone_info = self.client.lookups.v1.phone_numbers(mobile_num).fetch(type=['carrier', ])
        # TODO  verify logic
        return True

    @staticmethod
    def is_valid_phone_format(phone, format='basic'):
        phone_pattern = {
            'basic': re.compile('^\d{10}$'),
        }
        res = re.search(phone_pattern[format], phone)
        return res


class Emailhandler:
    def __init__(self):
        pass

    def hash_str(self):
        pass

    def send_registration_email(self, email):
        pass

if __name__ == "__main__":
    pass
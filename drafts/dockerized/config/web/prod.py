import os
from pathlib import Path
from logging import config as log_config

# from django.urls import reverse_lazy
# LOGIN_URL = reverse_lazy('account:login')
# LOGIN_REDIRECT_URL='/dashboard'

BASE_DIR = Path(__file__).resolve().parent.parent.parent
MEDIA = os.path.join(BASE_DIR, 'media')
URL = 'https://localhost/media/'

QR_LOGO = os.environ.get('QR_LOGO', os.path.join(MEDIA, 'logo_thumbnail.png'))
QR_CODE = os.environ.get('QR_CODE', os.path.join(MEDIA, 'qr'))
PHOTO = os.environ.get('PHOTO',os.path.join(MEDIA, 'photo'))
DL = os.environ.get('DL', os.path.join(MEDIA, 'dl'))
SMS_IMG = os.environ.get('SMS_IMG', os.path.join(MEDIA, 'sms'))
LOG_DIR = os.environ.get('LOGS', os.path.join(BASE_DIR, 'logs'))



LOGO_URL = os.environ.get('LOGO_URL', URL + 'logo_thumbnail.png' )
QR_URL = os.environ.get('QR_URL', URL + 'qr')
PHOTO_URL = os.environ.get('PHOTO_URL', URL + 'photo')
SMS_IMG_URL = os.environ.get('SMS_IMG_URL', URL + 'sms')

# messaging
SMS_ACCT = os.getenv('SMS_ACCT', None)
SMS_TOKEN = os.getenv('SMS_TOKEN', None)
SMS_FROM = os.getenv('SMS_FROM_NUMBER', None)
SMS_IT_NUMBER = os.getenv('SMS_IT_NUMBER', None)
SMS_ADMIN_NUMBER = os.getenv('SMS_ADMIN_NUMBER', None)
SMS_MGMT_NUMBER = os.getenv('SMS_MGMT_NUMBER', '').split(',')

VENDOR = os.getenv('VENDOR', 'local')
SITE_HEADER = os.getenv('SITE_HEADER', 'local')
SITE_TITLE = os.getenv('SITE_TITLE', 'local')
INDEX_TITLE = os.getenv('INDEX_TITLE', 'local')

# push notification
AUTH_KEY_PATH=os.environ.get('AUTH_KEY_PATH', None) # APNs .p8 file
TEAM_ID = os.environ.get('TEAM_ID', None)  # apple developer team id
KEY_ID = os.environ.get('KEY_ID', None) # APNs Auth Key id
BUNDLE_ID = os.environ.get('BUNDLE_ID', None) # app's bundle identifier
iOS_NOTIFICATION_SANBOX = os.environ.get('iOS_NOTIFICATION_SANBOX', True)
FCM_SERVER_KEY = os.environ.get('FCM_SERVER_KEY', None) # Firebase Cloud Messaging server key
FCM_ENDPOINT_URL = os.environ.get('FCM_ENDPOINT_URL', 'https://fcm.googleapis.com/fcm/send')


STORE = (
    ('1', 'alpha'),
    # ('2', 'beta'),
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": "DEBUG",
        "handlers": []
    },
    "handlers": {
        "by_pass":{
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'by_pass_registration.log'),
            'formatter': 'by_pass',
        },
        "registration":{
            'level': "INFO",
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'registration.log'),
            'formatter': 'registration',
        },
        "check_in":{
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'check_in.log'),
            'formatter': 'check_in',
        },
        "message":{
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'message.log'),
            'formatter': 'message',
        },
    },
    "loggers": {
        'by_pass':{
            'handlers': ['by_pass', ],
            'level': 'INFO',
            'propagate': False,
        },
        'registration':{
            'handlers': ['registration',],
            'level': 'INFO',
            'propagate': False,
        },
        'check_in':{
            'handlers': ['check_in',],
            'level':'INFO',
            'propagate': False,
        },
        'message':{
            'handlers': ['message'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    "formatters": {
        'by_pass': {
            'format': (
                "%(asctime)s %(levelname)s %(message)s "
            ),
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
        'registration':{
            'format': (
                "%(asctime)s %(levelname)s %(message)s "
            ),
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
        'check_in': {
            'format': (
                "%(asctime)s %(levelname)s %(message)s "
            ),
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
        'message':{
            'format': (
                "%(asctime)s %(levelname)s %(message)s "
            ),
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
}

log_config.dictConfig(LOGGING)





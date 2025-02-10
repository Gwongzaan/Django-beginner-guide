import os
import importlib

base_settings = importlib.import_module('config.base')
print('config.base.py imported')

try:
    for setting in dir(base_settings):
        if setting == setting.upper():
            locals()[setting] = getattr(base_settings, setting)
except Exception as e:
    print(e)

settings_module = importlib.import_module('config.web.prod')
print(f"using config.web.prod ")
try:
    for setting in dir(settings_module):
        # Only fully-uppercase variables are supposed to be settings
        if setting == setting.upper():
            locals()[setting] = getattr(settings_module, setting)
except Exception as e:
    # could be ignore, the print is for debugging purposes
    print(e)
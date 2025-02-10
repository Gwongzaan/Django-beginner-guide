from django.db import models

# Create your models here.
class VerificationCode(models.Model):
    phone = models.CharField(max_length=10)
    code = models.CharField(max_length=5)
    add_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.phone

class EmailVerification(models.Model):
    code = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    send_time = models.DateTimeField(auto_now_add=True) 
from email import message
from django.db import models
from django.contrib.auth.models import User

# Create your models here

class prvMsg(models.Model):
    title = models.TextField(max_length=200)
    msg = models.TextField(max_length=1000)
    sendDate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    # isOpen = models.BooleanField
    sender_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='od_kogo')
    reciver_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='do_kogo')

    def __str__(self):
       return str(self.sender_id)

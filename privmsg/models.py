from email import message
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import random

# Create your models here


class prvMsg(models.Model):
    title = models.TextField(max_length=200)
    msg = models.TextField(max_length=1000)
    sendDate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    # isOpen = models.BooleanField
    sender_id = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE, related_name='od_kogo')
    reciver_id = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE, related_name='do_kogo')
    is_open = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        time = timezone.now()
        minutes = time.minute
        seconds = time.second
        rand = random.randint(10000, 5010000)

        if not self.slug:
            self.slug = slugify(self.title)
            self.slug += str(minutes) + str(seconds) + str(rand)

        super(prvMsg, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.sender_id)

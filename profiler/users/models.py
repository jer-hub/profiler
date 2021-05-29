from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.html import mark_safe
import os, random

now = timezone.now()
# Create your models here.

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrst123456890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return 'profile_pic/{year}-{month}-{imageid}-{basename}-{randomstring}{ext}'.\
        format(imageid = instance,
               basename = basefilename,
               randomstring = randomstr,
               ext = file_extension,
               year = _now.strftime('%Y'),
               month = _now.strftime('%m'),
               day = _now.strftime('%d'))

class User(models.Model):
    user_name = models.CharField(max_length=200, verbose_name='First Name')
    user_lname = models.CharField(max_length=200, verbose_name='Last Name')
    user_email = models.EmailField(unique=True, max_length=200, verbose_name='Email')
    user_position = models.CharField(max_length=200, verbose_name='Position')
    user_image = models.ImageField(upload_to=image_path, default='profile_pic/image.jpg')

    def image_tag(self):
        return mark_safe('<img src="/users/media/%s" width="50" height="50" />'%(self.user_image))

    pub_date = models.DateField(default=now)

    def __str__(self):
        return f'Email : {self.user_email}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(default='null')
    body = models.TextField(default='null')
    created_on = models.DateTimeField(default=now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
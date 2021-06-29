from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to = 'profile_pic',default = 'download.png')

    def __str__(self) -> str:
        return f'{self.user.username} profile'

class blog(models.Model):
    # TAG_CHOICES =[
    #     ('politics','politics'),
    #     ('technology','technology'),
    #     ('sports','sports'),
    #     ('literature','literature'),
    #     ('langauge','langauge'),
    #     ('humanities','humanities'),
    #     ('environment','environment'),
    #     ('history','history'),
    #     ('economics','economics'),
    #     ('books','books'),
    #     ('marketing','marketing'),
    #     ('programming','programming'),
    #     ('Health','Health'),
    # ]
    tag = models.CharField(max_length=50, blank=True,)
    title = models.CharField(max_length=120, blank=False, null=False)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(
        max_length=5000, blank=True, null=True, default=None)
    author = models.CharField(max_length=120, blank=False)
    created = models.DateField(auto_now=True)
    headerImage = models.ImageField(upload_to='')

    def __str__(self) -> str:
        return f'{self.title} - {self.author}'

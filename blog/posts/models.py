from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=False)
    category = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to = 'posts/photos', blank=True, null=True)
    body = models.TextField(max_length=3000)
    facebookVideoLink = models.CharField(max_length=200, blank=True)
    facebookLiveVideoLink = models.CharField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    lastUpdated = models.DateTimeField(auto_now = True)
    eventDateTime = models.DateTimeField(null=True,blank =True,auto_now_add=False, auto_now=False)
    eventType= models.IntegerField(blank =True)

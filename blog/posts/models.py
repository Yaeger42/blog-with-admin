from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=False)
    category = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to = 'posts/photos', blank=True)
    body = models.TextField(max_length=3000)
    created = models.DateTimeField(auto_now_add = True)
    lastUpdated = models.DateTimeField(auto_now = True)

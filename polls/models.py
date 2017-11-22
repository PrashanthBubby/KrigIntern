from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    city=models.CharField(max_length=100,default='')
class Posts(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.TextField(max_length=15)
    post=models.TextField()
    date=models.DateTimeField(default='')
    

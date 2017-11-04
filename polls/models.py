from django.db import models

class signin(models.Model):
    login=models.CharField(max_length=15)
    password=models.TextField()

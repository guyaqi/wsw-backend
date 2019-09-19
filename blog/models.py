from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=64)
  password = models.CharField(max_length=64)

  nickname = models.CharField(default="不愿意透露姓名的外星来客",max_length=16)
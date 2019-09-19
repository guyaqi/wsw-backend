from django.db import models

# Create your models here.

class User(models.Model):
  username = models.CharField(max_length=64)
  password = models.CharField(max_length=64)

  nickname = models.CharField(default="不愿意透露姓名的外星来客",max_length=16)

  def __str__(self):
    return self.nickname

class Article(models.Model):
  title = models.CharField(max_length=64)
  author = models.ForeignKey(User, on_delete=models.PROTECT)

  create_time = models.DateField('date published')
  modify_time = models.DateField('date last modified')

  content = models.TextField(default="")
  name = models.CharField(max_length=64)
  tag = models.CharField(max_length=64)

  def __str__(self):
    return self.title
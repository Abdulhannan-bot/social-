from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django import forms

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

import random

class Account(models.Model):
  user = models.OneToOneField(User, null = True, blank = True, on_delete = models.CASCADE)
  email = models.EmailField(max_length = 224, null = True)
  full_name = models.CharField(max_length = 100, null = True)
  # username = models.CharField(max_length = 20, default = "", null = True, blank = True)
  # password = models.CharField(max_length = 30, null = True)
  created_at = models.DateTimeField(auto_now_add = True, null = True)
  profile_pic = models.ImageField(default="user.png", null = True, blank = True)

  def __str__(self):
    return str(self.user)

class Post(models.Model):
  post = RichTextUploadingField(blank = True, null = True)
  user_id = models.ForeignKey(Account, null = True, on_delete=models.SET_NULL)
  created_at = models.DateTimeField(auto_now_add = True, null = True)


  def __str__(self):
    return str(self.created_at)
  
class Comment(models.Model):
  text = models.TextField(null = True)
  post_id = models.ForeignKey(Post, null = True, blank = True, on_delete=models.SET_NULL)
  user_id = models.ForeignKey(Account, null = True, blank = True, on_delete=models.SET_NULL)
  created_at = models.DateTimeField(auto_now_add = True, null = True)


  def __str__(self):
    return str(self.text[:10])+"....."

class Like(models.Model):
  user_id = models.ForeignKey(Account, null = True, blank = False, on_delete=models.SET_NULL, related_name="post_by")
  post_id = models.ForeignKey(Post, null = True, blank = False, on_delete=models.SET_NULL)
  liked_by = models.ForeignKey(Account, null = True, blank = False, on_delete=models.SET_NULL, )

  def __str__(self):
    return str(self.liked_by) + " likes a post by " + str(self.user_id)

class Follower(models.Model):
  follower_id = models.ForeignKey(Account, related_name = 'follower', null = True, on_delete=models.SET_NULL)
  followee_id = models.ForeignKey(Account, related_name = 'followee', null = True, on_delete=models.SET_NULL)

  def __str__(self):
    return str(self.follower_id)+" follows "+str(self.followee_id)

class Tag(models.Model):
  tag_name = models.CharField(max_length = 50, null = True)

class PhotoTag(models.Model):
  post_id = models.ForeignKey(Post, null = True, on_delete=models.SET_NULL)
  tag_id = models.ForeignKey(Tag, null = True, on_delete=models.SET_NULL)


# @receiver(post_save, sender = Account)
# def user_generator(sender, created, instance, **kwargs):
#   # if created:
#   if instance.username != "" and instance.username is not None:
#     user = User.objects.create(username = instance.username, email = instance.email)
#     user.set_password(instance.password)

#     user.save()
#     instance.user = User.objects.get(username = instance.username)

#   elif(instance.full_name is not None):
#     a = random.randint(100,999)
#     user_name = "".join(str(instance.full_name).lower().split(" ")[:2])+str(a)
#     user_password = "".join(str(instance.full_name).lower().split(" ")[:2])+str(a)
#     instance.username = user_name
#     user = User.objects.create(username = instance.username, email = instance.email)
#     user.set_password(instance.password)
#     user.save()
#     instance.user = User.objects.get(username = instance.username)


@receiver(post_save, sender = User)
def user_generator(sender, created, instance, **kwargs):
  if created:
    Account.objects.create(
      user = instance,
      email = instance.email,
      full_name = instance.first_name+" "+instance.last_name
    )


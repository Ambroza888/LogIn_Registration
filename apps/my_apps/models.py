from django.db import models
import re

class UserManager(models.Manager):
  def basic_validator(self,postData):
    errors = {}
    if len(postData['first_name']) < 2:
      errors['first_name'] = "Please use more than 2 characters for First Name"
    if len(postData['last_name']) < 2:
      errors['last_name'] = "put more than 2 characters for Last Name"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(postData['email']):
      errors['email'] = "Invalid Email adress Baby !!!"
    if postData["password"] != postData["re_password"]:
      errors['password'] = "Password is not matching baby"
    if len(postData['password']) <=8:
      errors['password_char'] = "Password need to 8 or more characters"

    return errors

class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  email = models.CharField(max_length=45)
  password = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()


class Message(models.Model):
  messege = models.TextField()
  user = models.ForeignKey(User, related_name="messege")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
  comment = models.TextField()
  message = models.ForeignKey(Message, related_name="comment")
  user = models.ForeignKey(User, related_name="comment")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
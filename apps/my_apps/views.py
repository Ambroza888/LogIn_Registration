from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
import re
from django.contrib import messages



def index(request):
  return render(request, "my_apps/index.html")


def reg_in_data(request):
  errors = User.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key , value in errors.items():
      messages.error(request, value)
    return redirect('/')
  else:
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    re_password = request.POST['re_password']
    if password == re_password:
      pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
      new_user = User.objects.create(first_name=first_name,last_name=last_name,email=email,password=pw_hash)
      request.session['userid'] = new_user.id
      return redirect('/success')
    else:
      return redirect('/')


def success(request):
  if not 'userid' in request.session:
    return redirect('/')
  else:
    return render(request, "my_apps/success.html", {"y":User.objects.get(id=request.session['userid'])})


def log_in_data(request):
  email = request.POST['email']
  password = request.POST['password']
  user = User.objects.filter(email=email)
  if user:
    logged_user = user[0]
    if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
      request.session['userid'] = logged_user.id
      return redirect('/success')

  return redirect('/')

def go_back(request):
  request.session.clear()
  return redirect('/')






def dojo_wall(request):
  if not "userid" in request.session:
    return redirect('/')
  else:
    context = {
    "the_user":User.objects.get(id = request.session['userid']),
    "all_mess":Message.objects.all(),
    "all_comments": Comment.objects.all()
  }
  return render(request, "my_apps/dojo_wall.html",context)

def add_post(request):
  mess = request.POST['messege']
  id = request.session['userid']
  the_user = User.objects.get(id=id)
  Message.objects.create(messege=mess, user=the_user)
  return redirect("/wall")


def add_comment(request):
  comment = request.POST['comment']
  message = Message.objects.get(id = request.POST['message_id'])
  user = User.objects.get(id=request.session['userid'])
  Comment.objects.create(comment=comment,message = message,user = user)

  return redirect('/wall')
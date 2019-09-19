from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse

from hashlib import sha256
import json

from .models import User

# Create your views here.

def getHash(s):
  return sha256(s.encode('utf-8')).hexdigest()

'''
Login Api

Example:

await fetch("http://127.0.0.1:8000/auth/login/", {
  method:"POST",
  body:JSON.stringify({
    "username": "guyaqi5858",
    "password":"@kckrukia1998"
    }),
  credentials: "include"
}).then(r=>r.json())

'''
def login(request):
  if request.method != 'POST':
    return HttpResponse(status=400)

  data = json.loads(request.body)

  username = ""
  password = ""
  if 'username' not in data or 'password' not in data:
    return HttpResponse(status=400)
  else:
    username = data['username']
    password = data['password']
  
  success = True
  detail = ""
  # token = ""

  '''only check but not save session'''
  qs = User.objects.filter(username=getHash(username), password=getHash(password))
  print(qs)
  if len(qs) == 0:
    success = False
    detail = "wrong username or password"
  elif len(qs) == 1:
    request.session['username'] = username

  responce = {"success": success, "detail": detail}
  return JsonResponse(responce)

'''
Greetings. Need login.

Example:

await fetch("http://127.0.0.1:8000/auth/greet/", {
  method:"POST",
  credentials: "include"
}).then(r=>r.json())

'''

def greet(request):
  msg = ""
  if "username" not in request.session:
    msg = "login need"
  else:
    msg = "Hello " + request.session['username']

  responce = {"msg": msg}
  return JsonResponse(responce)

'''
Logout.

Example:

await fetch("http://127.0.0.1:8000/auth/logout/", {
  method:"POST",
  credentials: "include"
}).then(r=>r.json())

'''
def logout(request):
  msg = ""
  if "username" not in request.session:
    msg = "you have not logined"
  else:
    msg = 'logout success'
    request.session.flush()

  responce = {"msg": msg}
  return JsonResponse(responce)
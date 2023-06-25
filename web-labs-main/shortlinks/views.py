import datetime
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
from django.template import loader
from django.core import serializers
from django.db.models import Q

from shortlinks.tasks import send_verification_email
from .models import User,Links
import django.contrib.auth as auth
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
    #print("Random string of length", length, "is:", result_str)

def index(request):
    return render(request,"index.jinja",{"userName" : request.user.username})

def register(request):

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "POST":
        try:
            data = request.POST
            email = data.get("email")
            password = data.get("pass")
            user_name = data.get("login")
            sex = data.get("sex")
            birth_date = data.get("birthDate")
            user = User.objects.create_user(user_name, email, password)
            user.sex = sex
            user.birth_date = birth_date
            user.save()
            auth.authenticate(request, username=user_name, password=password)
            send_verification_email(email)
            print("successful registration")
            return redirect('index')
        except:
            return redirect('register')
    return render(request,"register.jinja")

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request,"login.jinja")

def log_out(request):
    auth.logout(request)
    return redirect('index')

def user_page(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request,"user_page.jinja",{ 
        "userName" : request.user.username,
        "email" : request.user.email,
        "gender": request.user.sex,
        "date" : request.user.birth_date})

def about(request):
    return render(request,"about.jinja",{"userName" : request.user.username})
# dwitter/views.py
def create_short_post(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body['link'])
        link = Links()
        link.original_link = body['link']
        link.short_link = get_random_string(10)
        if not request.user.is_anonymous:
            link.user_id = request.user
        else:
            link.user_id = None
            
        link.save()
        return JsonResponse({"id" : link.id, "short_link" : link.short_link})
    else:
        return HttpResponseBadRequest()

def get_all_links(request):
    links = Links.objects.all().filter(user_id = request.user.id)
    data = serializers.serialize('json', links)
    return JsonResponse(data, safe= False)

def delete_link(request):

    if request.method != "DELETE":
        return HttpResponseForbidden()
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    Links.objects.get(Q(user_id = request.user.id), Q(id = body["id"])).delete()
    return HttpResponse()

def update_link(request):
    if request.method != "PATCH":
        return HttpResponseForbidden()
    
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    link = Links.objects.get(Q(user_id = request.user.id), Q(id = body["id"]))
    link.original_link = body["newText"]
    link.save()
    return HttpResponse()

def redirect_to_original(request):
    redirect_link = ""
    try:
        redirect_link = Links.objects.get(short_link = request.path[1:]).original_link
    except:
        redirect_link = "index"

    return redirect(redirect_link)

# ...
"""
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})
"""

from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return HttpResponse("hallo")

def login_(request):
    if request.method == 'POST':
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout_(request):
    return redirect("/")

def sign_up_(request):
    if request.method == 'POST':
        if request.POST.get('username') is "admin"
        if request.POST.get('username') is not None and len(request.POST.get('username')) >= 3:
            if request.POST.get('psw') is not None and len(request.POST.get('psw')) >= 8:
                if (request.POST.get('psw') == request.POST.get('pswc')):
                    if User.objects.get(username = request.POST.get('username')) and request.POST.get('username')):
                        return render(request, 'signup.html', {'error':"This username has already been taken choose another one"})
                    else:
                        return render(request, 'login.html')
                else:
                    return render(request, 'signup.html', {'error':"The passwords are not the same"})
            else:
                return render(request, 'signup.html', {'error':"Password must have atleast 8 Characters"})   
        else:
            return render(request, 'signup.html', {'error':"Username must have at least 3 or more Characters"})
    elif request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
    
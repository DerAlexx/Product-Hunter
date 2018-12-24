from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import product
import imghdr,datetime

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        print(request)
        if request.POST.get('title') is not None and len(request.POST.get('title')) > 3:
            if request.POST.get('dis') is not None and len(request.POST.get('dis')) >= 20:
                if len(request.POST.get('dis')) <= 500:
                    if request.POST.get('url') is not None and len(request.POST.get('url')) > 2:
                        if "jpg" in (imghdr.what(request.FILES.get('icon')).lower()) or "jpeg" in (imghdr.what(request.FILES.get('icon')).lower()) or "png" in (imghdr.what(request.FILES.get('icon')).lower()):
                            print(imghdr.what(request.FILES.get('icon')).lower())
                            if "jpg" in (imghdr.what(request.FILES.get('image')).lower()) or "jpeg" in (imghdr.what(request.FILES.get('image')).lower()) or "png" in (imghdr.what(request.FILES.get('image')).lower()):
                                prodt = product()
                                prodt.title = request.POST.get('title')
                                prodt.body = request.POST.get('dis')
                                if request.POST.get('url').startswith('http://') or request.POST.get('url').startswith('https://'):
                                    prodt.url = request.POST.get('url')
                                else:
                                    prodt.url = 'http://' + request.POST.get('url')
                                prodt.icon = request.FILES.get('icon')
                                prodt.image = request.FILES.get('image')
                                prodt.pub_date = datetime.datetime.now()
                                prodt.hunter = request.user
                                prodt.save()
                                return redirect("/")
                            else:
                                return render(request, 'create.html', {'error':"Images must be JPG or PNG Format"}) 
                        else:
                            return render(request, 'create.html', {'error':"Icons must be JPG or PNG Format"}) 
                    else:
                        return render(request, 'create.html', {'error':"Enter a valid URL"}) 
                else:
                    return render(request, 'create.html', {'error':"Maximumlength exceeded! Only 500 Characters are allowed in the Description."})
            else:
                 return render(request, 'create.html', {'error':"The minimumlength of a Description should be 20 Characters!"})
        else:
            return render(request, 'create.html', {'error':'A Product should have a Title with aleast the length of 4 Characters!'})
    else:
        print("h2hh")
        return render(request, 'create.html')

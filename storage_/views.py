from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .models import data
import os
from cloudservice.settings import BASE_DIR
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
        data_ = data.objects.all()
        context = {'data' : data_}
        return render(request, "storage_/index.html", context = context)
    
    

def login_(request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('storage')
        return render(request, "storage_/login.html")


@login_required(login_url='login')
def logout_(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def upload(request):
    if request.method == "POST":
        if request.FILES.get('docfile', False):
            file_name = request.FILES['docfile']
            file_size = request.FILES['docfile'].size
            file_description = request.POST['description']
            file = request.FILES['docfile']
            print(file_name, file_size, file_description)
            data_obj = data(file_name = file_name, file_description = file_description, file = file, file_size = file_size )
            data_obj.save()
    return render(request, 'storage_/upload.html')

@login_required(login_url='login')
def delete(request, id):
    dobj = data.objects.get(id = id)
    media = "files/" + dobj.file.name
    file = os.path.join(BASE_DIR, media)
    os.remove(file)
    dobj.delete()
    return redirect('storage')

@login_required(login_url='login')
def more_info(request, id):
    dobj = data.objects.get(id = id)
    context = {'desc' : dobj.file_description}
    return render(request, 'storage_/more_info.html', context=context)

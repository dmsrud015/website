from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from django.shortcuts import render, redirect 


# Create your views here.

def index(request):
    return render(request,'index.html')

def buy(request):
    return render(request,'buy.html')

def collect(request):
    return render(request,'collect.html')

def login(request):
    return render(request,'login.html')

def mypage(request):
    return render(request,'mypage.html')
    
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            name=request.POST['name'],
                                            id=request.POST['id'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
                                            
            auth.login(request, user)
            return redirect('')
        return render(request, 'signup.html')
    return render(request, 'signup.html')
    
	
    
def find_pw(request):
    return render(request,'find_pw.html')

def new_pw(request):
    return render(request,'new_pw.html')

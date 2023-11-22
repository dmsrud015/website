from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from hello.forms import UserForm
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
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            id = form.cleaned_data.get('id')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(name=name,username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'hello/signup.html', {'form': form})
	
    
def find_pw(request):
    return render(request,'find_pw.html')

def new_pw(request):
    return render(request,'new_pw.html')

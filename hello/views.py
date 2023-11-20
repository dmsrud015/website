from django.shortcuts import render

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
    return render(request,'signup.html')
    
def find_pw(request):
    return render(request,'find_pw.html')

def new_pw(request):
    return render(request,'new_pw.html')
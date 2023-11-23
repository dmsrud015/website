from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from hello.forms import UserForm
from django.core.mail.message import EmailMessage
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from hello.forms import UserForm, PasswordResetForm
from django.contrib.auth import authenticate, login
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
            user = authenticate(id=id,username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'hello/signup.html', {'form': form})
	
    
def find_pw(request):
    return render(request,'find_pw.html')

def new_pw(request):
    return render(request,'new_pw.html')

def send_email(request):
    subject = "message"
    to = ["dmsrud015973@gmail.com"]
    from_email = "dmsrud015973@gmail.com"
    message = "메지시 테스트"
    EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()

class PasswordChangeView(auth_views.PasswordChangeView):
    """
    비밀번호 변경
    """
    template_name = 'common/password_change.html'
    success_url = reverse_lazy('index')

    # def form_valid(self, form):  # 유효성 검사 성공 이후 로직
    #     messages.success(self.request, '암호를 변경했습니다.')  # 성공 메시지
    #     return super().form_valid(form)  # 폼 검사 결과를 반환


class PasswordResetView(auth_views.PasswordResetView):
    """
    비밀번호 초기화 - 사용자ID, email 입력
    """
    template_name = 'hello/password_reset.html'
    # success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm
    # email_template_name = 'registration/password_reset_email.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    """
    비밀번호 초기화 - 메일 전송 완료
    """
    template_name = 'hello/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    비밀번호 초기화 - 새로운 비밀번호 입력
    """
    template_name = 'hello/password_reset_confirm.html'
    success_url = reverse_lazy('login')

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.index, name='index'),
    path('buy', views.buy, name='buy'),
    path('collect', views.collect, name='collect'),
    path('login/', auth_views.LoginView.as_view(template_name='hello/login.html'), name='login'),
    path('mypage', views.mypage, name='mypage'),
    path('signup', views.signup, name='signup'),
    path('find_pw', views.find_pw, name='find_pw'),
    path('new_pw', views.new_pw, name='new_pw'),
    #google smtp
    path('send_email/',views.send_email, name='send_email'),
    #비밀 번호 초기화 및 변경
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),                      
	path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

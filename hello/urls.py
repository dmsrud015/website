from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('buy', views.buy, name='buy'),
    path('collect', views.collect, name='collect'),
    path('login', views.login, name='login'),
    path('mypage', views.mypage, name='mypage'),
    path('signup', views.signup, name='signup'),
    path('find_pw', views.find_pw, name='find_pw'),
    path('new_pw', views.new_pw, name='new_pw'),
]
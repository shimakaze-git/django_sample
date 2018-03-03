from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import views as auth_views

from .forms import RegisterForm, LoginForm

# Create your views here.


def login(request):
    '''
    ログイン関連
    '''
    template_name = 'auth_sample/login.html'
    
    context = {
        'template_name': template_name,
        'authentication_form': LoginForm
    }

    return auth_views.login(request, **context)
    
    
def logout(request):
    '''
    ログアウト関連
    '''
    template_name = 'auth_sample/index.html'
    
    context = {
        'template_name': template_name,
    }
    
    return auth_views.logout(request, **context)

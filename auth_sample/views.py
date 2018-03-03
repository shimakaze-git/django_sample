from django.shortcuts import render
from django.views.generic import View


# Create your views here.


class LoginView(View):
    '''
    ログイン関連
    '''
    def get(self, request):
        
        template_name = 'auth_sample/login.html'
        
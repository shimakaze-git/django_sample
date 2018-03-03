from django.urls import path
from . import views

#View Class
from .views import RegistAccountsView, IndexAccountsView, ProfileAccountsView

app_name="auth_sample"
urlpatterns = [
    path('', IndexAccountsView.as_view(), name="index"),
    path('profile', ProfileAccountsView.as_view(), name="profile"),
    path('regist', RegistAccountsView.as_view(), name="regist"),
    path('login', views.login, name='login'),
    path('logout', views.logout ,name='logout'),
]
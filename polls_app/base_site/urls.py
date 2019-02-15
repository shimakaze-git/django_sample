from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'base_site'
urlpatterns = [
    # 60*15 = 900 second = 15 min
    path('', cache_page(60 * 15)(views.index), name='index'),
]

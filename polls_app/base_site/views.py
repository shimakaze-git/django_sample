from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    # return HttpResponse('test')
    return render(request, 'index.html', context)

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'templates/hello.html')
# Create your views here.

from django.shortcuts import render


def index(request):
    return render(request, 'templates/hello.html')
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, request
from .models import List

# Create your views here.

#from episode 1-3 
# def home(request,a):
#     message = '<h1>hello world---{}</h1><br><h2>hi i am safat</h2>'.format(a)
#     return HttpResponse(message)

def home(request):
    # message = 'This is RMA'
    all_items = List.objects.all()
    # return render(request, 'layouts.html', {'message':message})
    return render(request, 'layouts.html', {'all_items':all_items})

def about(request):
    message = 'This is about page'
    return render(request, 'about.html', {'message':message})


def say_hello(request):
    x = 1
    y = 2
    return render(request, 'hello.html', {'name':'Mosh'})

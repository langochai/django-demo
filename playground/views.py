from django.shortcuts import render
from django.http import HttpResponse

# basically this is request handler

def say_hello(req):
    return render(req, 'hello.html',{'name':'Nigga'})
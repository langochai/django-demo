import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def send_json(req):
    return HttpResponse(json.dumps({'message':'not very ok'}), content_type='application/json')
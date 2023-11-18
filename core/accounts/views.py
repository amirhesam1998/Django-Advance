from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
import time
import requests
# Create your views here.

def send_email(request):
    time.sleep(3)
    return HttpResponse('<h1>ok<\h1>')

def test(request):
    response = requests.get('https://b0d46176-e776-489e-8198-8335c085a042.mock.pstmn.io/test/delay/5').json()
    return JsonResponse(response)

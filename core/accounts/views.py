from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
import time
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
# Create your views here.

def send_email(request):
    time.sleep(3)
    return HttpResponse('<h1>ok<\h1>')

# def test(request):
#     if cache.get("ok") is None:
#         response = requests.get('https://b0d46176-e776-489e-8198-8335c085a042.mock.pstmn.io/test/delay/5')
#         cache.set("ok",response.json(),60)
#     return JsonResponse(cache.get("ok"))

@cache_page(60)
def test(request):

    response = requests.get('https://b0d46176-e776-489e-8198-8335c085a042.mock.pstmn.io/test/delay/5')

    return JsonResponse(response.json())

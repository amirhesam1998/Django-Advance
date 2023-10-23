from django.shortcuts import render

# Create your views here.

def Indexview(request) :
    name = "ali"
    context = {"name" : name}
    return render(request , 'index.html' , context)

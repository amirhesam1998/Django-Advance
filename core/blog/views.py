from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
# Create your views here.

def indexview(request) :
    """
    function based view (fbv)
    """
    name = "ali"
    context = {"name" : name}
    return render(request , 'index.html' , context)

class Indexview(TemplateView):
    """
    class based view (cbv)
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):                          #set context
        context = super().get_context_data(**kwargs)               #inheritance by TemplateView by super() method
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context

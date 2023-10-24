from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView , RedirectView
from  django.views.generic import ListView
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

#function based view to show template (example)
'''
def indexview(request) :
    """
    function based view (fbv)
    """
    name = "ali"
    context = {"name" : name}
    return render(request , 'index.html' , context)
'''
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


''' fbv for redirect

from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect("https://maktabkhooneh.com")

'''


'''
 cbv for redirect
'''

class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.com"

    def get_redirect_url(self, *args, **kwargs):         # for example if run this url 'blog/go-to-maktab/1' Along with this URL, the post information along with the ID given by the user in the blog application will be transferred to site maktabkhone
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    
class Postlist(ListView):
    model = Post                         #once solution         
    #queryset = Post.objects.all()         #two solution and get_queryset method tree solution
    context_object_name = "posts"                 #edit default context object name (object_list to any want you (example : posts) in html code)    
    paginate_by = 2
    ordering = '-id'

    #def get_queryset(self):
    #    posts = Post.objects.filter(status = False)
    #    return posts
    

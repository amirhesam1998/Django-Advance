from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import PostForm
from .models import Post


# Create your views here.

# function based view to show template (example)
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

    def get_context_data(self, **kwargs):  # set context
        context = super().get_context_data(
            **kwargs
        )  # inheritance by TemplateView by super() method
        context["name"] = "ali"
        context["posts"] = Post.objects.all()
        return context


""" fbv for redirect

from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect("https://maktabkhooneh.com")

"""


"""
 cbv for redirect
"""


class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.com"

    def get_redirect_url(
        self, *args, **kwargs
    ):  # for example if run this url 'blog/go-to-maktab/1' Along with this URL, the post information along with the ID given by the user in the blog application will be transferred to site maktabkhone
        post = get_object_or_404(Post, pk=kwargs["pk"])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostlistView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    model = Post  # once solution
    # queryset = Post.objects.all()         #two solution and get_queryset method tree solution
    context_object_name = "posts"  # edit default context object name (object_list to any want you (example : posts) in html code)
    # paginate_by = 2
    ordering = "-id"

    # def get_queryset(self):
    #    posts = Post.objects.filter(status = False)
    #    return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    
    
class PostlistApiView(TemplateView):
    template_name = 'blog/post_list_api.html'


"""
class PostCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post"
 
    def form_valid(self, form):                                                       #form save , if you dont write this function is not show to user
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(
    LoginRequiredMixin, CreateView
):  # CreateView save data in database by default, but FormView process data and dont save by default in databases, just use form_valid method can it.
    model = Post
    # fields = ['author','title','content','status','category','published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(
        self, form
    ):  # This function creates the form using the logged in user without entering the author's logged in email in the form and we clear the author field in the forms.py.
        form.instance.author = (
            self.request.user
        )  # In the 'form', set the 'author' part of the created 'instance' equal to the user who entered ((email)) of the user (creator or author field = user information login )
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"



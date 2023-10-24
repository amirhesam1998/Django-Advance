from django.urls import path
from .views import  Indexview , RedirectToMaktab , Postlist
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = [
    #path("fbv-index", indexview , name="fbv-index"),
    #path("cbv-index", TemplateView.as_view(template_name="index.html", extra_context = {"name" : "ali"})),
    path("cbv-index", Indexview.as_view() , name = "cbv-index"),   #run IndexView  classes
    path("go-to-varzesh3" , RedirectView.as_view(url = "https://varzesh3.com/") , name="redirect-to-varzesh3.com" ),  
    path("go-to-redirect-index" , RedirectView.as_view(pattern_name = "blog:cbv-index") , name="redirect-to-cbv-index" ), #go to blog app in open cbv-index path name
    path("go-to-maktab/<int:pk>" , RedirectToMaktab.as_view() , name="redirect-to-maktabkhone" ),
    path("post/" , Postlist.as_view() , name="Post-lists" ),   # (/) important
]
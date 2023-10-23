from django.urls import path
from .views import indexview , Indexview
from django.views.generic import TemplateView

urlpatterns = [
    path("fbv-index", indexview , name="fbv-index"),
    #path("cbv-index", TemplateView.as_view(template_name="index.html", extra_context = {"name" : "ali"})),
    path("cbv-index", Indexview.as_view() , name = "cbv-index")
]
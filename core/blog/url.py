from django.urls import path
from .views import Indexview
from django.views.generic import TemplateView

urlpatterns = [
    path("fbv-index", Indexview , name="fbv-index"),
    path("cbv-index", TemplateView.as_view(template_name="index.html", extra_context = {"name" : "ali"})),
]
from django.urls import path
from .views import postList

app_name = "api-v1"

urlpatterns = [
    path('post/',postList,name="post-list"),
]
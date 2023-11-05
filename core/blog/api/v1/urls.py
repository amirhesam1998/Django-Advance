from django.urls import path
from .views import PostList , postDetail

app_name = "api-v1"

urlpatterns = [
    #path('post/',postList,name="post-list"),
    path('post/',PostList.as_view(),name="post-list"),
    path('post/<int:id>/',postDetail,name="post-detail"),
]
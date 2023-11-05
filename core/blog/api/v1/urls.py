from django.urls import path
from .views import PostList , PostDetail , PostViewSets

app_name = "api-v1"

urlpatterns = [
    #path('post/',postList,name="post-list"),
    #path('post/<int:id>/',postDetail,name="post-detail")
    #path('post/',PostList.as_view(),name="post-list"),
    #path('post/<int:pk>/',PostDetail.as_view(),name="post-detail"),
    path('post/',PostViewSets.as_view({'get' : 'list','post':'create'}),name="post-list"),
    path('post/<int:pk>/',PostViewSets.as_view({'get' : 'retrieve','put' : 'update' , 'delete':'destroy', 'patch' : 'partial_update'}),name="post-detail"),
]
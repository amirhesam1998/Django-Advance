from django.urls import path
from .views import PostList, PostDetail, PostModelViewSets, CategoryModelViewSets
from rest_framework.routers import DefaultRouter

app_name = "api-v1"
router = DefaultRouter()
router.register("post", PostModelViewSets, basename="post")
router.register("category", CategoryModelViewSets, basename="category")


urlpatterns = [
    # path('post/',postList,name="post-list"),
    # path('post/<int:id>/',postDetail,name="post-detail")
    # path('post/',PostList.as_view(),name="post-list"),
    # path('post/<int:pk>/',PostDetail.as_view(),name="post-detail"),
    # path('post/',PostViewSets.as_view({'get' : 'list','post':'create'}),name="post-list"),
    # path('post/<int:pk>/',PostViewSets.as_view({'get' : 'retrieve','put' : 'update' , 'delete':'destroy', 'patch' : 'partial_update'}),name="post-detail"),
]

urlpatterns += router.urls

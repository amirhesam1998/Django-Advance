from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(["GET","POST"])
@permission_classes([IsAuthenticated])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status = True)
        serializer = PostSerializer(posts , many = True)
        data = serializer.data
        return Response(data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)               #request.data means,show data information send from client to server
        serializer.is_valid(raise_exception=True)                      #validations
        serializer.save()                                              #save serializer
        return Response(serializer.data)   
                                


@api_view(["GET" , "PUT" , "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):
    '''
    solution 1:
    '''
    #try:
        #post = Post.objects.get(pk=id)
        #serializer = PostSerializer(post)            #get post and put in the PostSerializer
        #data = serializer.data                     #convert object to json
        #return Response(data)
    #except Post.DoesNotExist:
        #return Response({"detail" : "Post Does not exist"} , status=status.HTTP_404_NOT_FOUND)
    '''
    solution 2:
    '''
    post = get_object_or_404(Post , pk=id , status = True)
    if request.method == "GET":
        serializer = PostSerializer(post) 
        data = serializer.data
        return Response(data)
    elif request.method == "PUT":
        serializer = PostSerializer(post , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail" : "item delete successfully"} , status=status.HTTP_204_NO_CONTENT)


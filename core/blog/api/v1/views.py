from rest_framework.decorators import api_view ,  permission_classes
from rest_framework.permissions import IsAuthenticated , IsAdminUser , IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView , ListCreateAPIView , RetrieveAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView
from rest_framework import mixins
#Example FBV :
"""@api_view(["GET","POST"])
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
        return Response(serializer.data)"""   

"""@api_view(["GET" , "PUT" , "DELETE"])
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
        return Response({"detail" : "item delete successfully"} , status=status.HTTP_204_NO_CONTENT)"""


#EXAMPLE CBV:
'''class PostList(APIView):
    """getting a list of post and creating a new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self,request):
        """retrieving a list of post"""
        posts = Post.objects.filter(status = True)
        serializer = PostSerializer(posts , many = True)
        data = serializer.data
        return Response(data)
    def post(self,request):
        """creating post with provided data"""
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  
        serializer.save()
        return Response(serializer.data)'''   

'''class PostList(GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin):
    """getting a list of post and creating a new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)

    def get(self, request, *args, **kwargs):
        """retrieving a list of post"""
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """creating post with provided data"""
        return self.create(request, *args, **kwargs)'''

class PostList(ListCreateAPIView):
    """getting a list of post and creating a new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)


'''class PostDetail(APIView):
    """getting detail of the post and edit plus delete the posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get(self,request,id):
        """retrieving a detail of post"""
        post = get_object_or_404(Post , pk=id , status = True)
        serializer = PostSerializer(post) 
        data = serializer.data
        return Response(data)
    def put(self,request,id):
        """editing the post data"""
        post = get_object_or_404(Post , pk=id , status = True)
        serializer = PostSerializer(post , data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)      
    def delete(self,request,id):
        """deleting the post """
        post = get_object_or_404(Post , pk=id , status = True)
        post.delete()
        return Response({"detail" : "item delete successfully"} , status=status.HTTP_204_NO_CONTENT)    '''

'''class PostDetail(GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    """getting detail of the post and edit plus delete the posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)

    def get(self, request, *args, **kwargs):
        """retrieving a list of post"""
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        """editing the post data"""
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        """deleting the post """
        return self.destroy(request, *args, **kwargs)
'''

class PostDetail(RetrieveAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView):
    """getting detail of the post and edit plus delete the posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status = True)
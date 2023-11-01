from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post

@api_view()
def postList(request):
    return Response("ok")


@api_view()
def postDetail(request,id):
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(post)            #get post and put in the PostSerializer
    data = serializer.data                     #convert object to json
    return Response(data)
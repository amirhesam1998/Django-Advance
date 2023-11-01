from rest_framework import serializers
from ...models import Post

#class PostSerializer(serializers.Serializer):                               #serializer
    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length = 255)


class PostSerializer(serializers.ModelSerializer):                           #ModelSerializer
    class Meta:
        model = Post
        fields = "__all__"
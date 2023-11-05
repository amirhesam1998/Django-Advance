from rest_framework import serializers
from ...models import Post , Category

#class PostSerializer(serializers.Serializer):                               #serializer
    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length = 255)


class PostSerializer(serializers.ModelSerializer):                           #ModelSerializer
    class Meta:
        model = Post
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
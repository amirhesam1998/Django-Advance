from rest_framework import serializers
from ...models import Post , Category

#class PostSerializer(serializers.Serializer):                               #serializer
    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length = 255)


class PostSerializer(serializers.ModelSerializer):                           #ModelSerializer
    snippet = serializers.ReadOnlyField(source = "get_snippet")
    relative_url = serializers.URLField(source = "get_absolute_api_url" , read_only = True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")

    class Meta:
        model = Post
        fields = ["id","author",'image',"title","content","snippet","status","category","relative_url","absolute_url","created_date","updated_date","published_date"]
        #read_only_fields = ["content"]

    def get_abs_url(self,obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
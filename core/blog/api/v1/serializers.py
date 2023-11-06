from rest_framework import serializers
from ...models import Post , Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


#class PostSerializer(serializers.Serializer):                               #serializer
    #id = serializers.IntegerField()
    #title = serializers.CharField(max_length = 255)


class PostSerializer(serializers.ModelSerializer):                           #ModelSerializer
    snippet = serializers.ReadOnlyField(source = "get_snippet")
    relative_url = serializers.URLField(source = "get_absolute_api_url" , read_only = True)
    absolute_url = serializers.SerializerMethodField(method_name="get_abs_url")
    #category = CategorySerializer()                            
    #category = serializers.SlugRelatedField(many = False , slug_field='name' , queryset = Category.objects.all())

    class Meta:
        model = Post
        fields = ["id","author",'image',"title","content","snippet","status","category","relative_url","absolute_url","created_date","updated_date","published_date"]
        #read_only_fields = ["content"]

    def get_abs_url(self,obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):                  #you should use this function whenever you want to change a value in the display only((it is not meant to  display the input values))
        request = self.context.get('request')               #get request objects
        rep = super().to_representation(instance)
        #print(request.__dict__)                             #show request detail
        rep['state'] = "list"                                 #when im get a list of post, default value
        if request.parser_context.get('kwargs').get('pk'):      #when im get a single of post ((for example '.../post/1')), if its does exist:
            rep['state'] = "single"                           #show single
            rep.pop('snippet',None)           #delete snippet field for show , None means if this object does not found dont show errors
            rep.pop('absolute_url',None)
            rep.pop('relative_url',None)
        else:                                         #when im get a list of post
            rep.pop('content',None)
        rep['category'] = CategorySerializer(instance.category).data                  #in the category field , set to the instance category value and serialize it and convert it to json , for manytomany or foreignkey value
        return rep


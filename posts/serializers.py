from posts.models import Post

from rest_framework import serializers

class PostsSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    file_name = serializers.CharField(required=False)
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_validation_exclusions(self):
        exclusions = super(PostsSerializer, self).get_validation_exclusions()
        return exclusions + ['file'] + ['file_name']
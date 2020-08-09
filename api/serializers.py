from rest_framework import serializers
from posts.models import Post, Comment
from rest_framework.decorators import action


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    post = serializers.IntegerField(source='post_id', required=False)

    class Meta:
        fields = ('id', 'text', 'author', 'post', 'created')
        model = Comment

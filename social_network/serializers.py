from rest_framework import serializers

from social_network.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "title", "description", "user")


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "title", "description")


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("id", "title", "description", "user")

from rest_framework import viewsets, mixins

from social_network.models import Post, UserFollowing
from social_network.serializers import (
    PostSerializer,
    PostCreateSerializer, PostDetailSerializer, UserFollowingSerializer, UserFollowerSerializer
)


class PostViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin

):
    queryset = Post.objects.all()

    def get_serializer_class(self):

        if self.action == "create":
            return PostCreateSerializer

        if self.action == "retrieve":
            return PostDetailSerializer

        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserFollowingViewSet(viewsets.ModelViewSet):
    serializer_class = UserFollowingSerializer
    queryset = UserFollowing.objects.all()

    def get_queryset(self):
        return UserFollowing.objects.filter(user_id__id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class UserFollowerViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin
):
    serializer_class = UserFollowerSerializer
    queryset = UserFollowing.objects.all()

    def get_queryset(self):

        return (
            UserFollowing.objects
            .exclude(user_id__id=self.request.user.id)
            .filter(following_user_id__id=self.request.user.id)
        )

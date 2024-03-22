from rest_framework import viewsets, mixins

from social_network.models import Post
from social_network.serializers import (
    PostSerializer,
    PostCreateSerializer
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

        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

from rest_framework import viewsets, permissions
from posts.models import Post, Comment
from api.serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_fields = ('post', 'id')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def perform_delete(self, serializer):
        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.kwargs['id']:
            queryset = get_object_or_404(Post, pk=self.kwargs['id']).comments
            return queryset
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs['id'])
        serializer.save(author=self.request.user,
                        post_id=self.kwargs['id'])

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, post_id=self.kwargs['id'])

    def perform_delete(self, serializer):
        serializer.save()

from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from blog.models import User, Post
from .serializers import UserSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["blog"]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Post.objects.filter(blog=user.blog).order_by("-created")
        return Post.objects.none()


class PostSubscriptionsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        subscribed_blogs = user.user_subscriptions.all().values_list("blog")
        posts = Post.objects.filter(blog__in=subscribed_blogs)
        return posts

    @action(detail=True, methods=["POST"])
    def mark_as_read(self, request, pk=None):
        user = request.user
        post = self.get_object()
        if post.blog.owner == user:
            return Response(
                {"detail": "You cannot mark your own post as read."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if post.is_read:
            return Response({"detail": "Post already read."})
        post.is_read = True
        post.save()
        return Response({"detail": "Post marked as read."})

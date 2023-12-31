from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings

from blog.models import User, Post, ReadPost, Subscriptions
from .serializers import UserSerializer, PostSerializer
from .permissions import IsAuthorOrReadOnly


class UserListView(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(detail=True, methods=["GET"])
    def subscribe(self, request, pk=None):
        user_to_follow = self.get_object()
        current_user = request.user

        if current_user == user_to_follow:
            return Response(
                {"detail": "You cannot subscribe to yourself."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscription, created = Subscriptions.objects.get_or_create(
            user=current_user, blog=user_to_follow.blog
        )

        if created:
            subscribed_posts = Post.objects.filter(blog=user_to_follow.blog)
            read_posts_to_create = [
                ReadPost(user=current_user, post=post)
                for post in subscribed_posts
            ]
            ReadPost.objects.bulk_create(read_posts_to_create)
            return Response({"detail": "Successfully subscribed."})
        else:
            return Response(
                {"detail": "Already subscribed."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ["blog"]
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = settings.POSTS_PER_PAGE

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(blog=user.blog).order_by("-created")


class PostSubscriptionsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        subscribed_blogs = user.user_subscriptions.all().values_list("blog")
        posts = Post.objects.filter(blog__in=subscribed_blogs)
        return posts

    @action(detail=True, methods=["GET"])
    def mark_as_read(self, request, pk=None):
        user = request.user
        post = self.get_object()
        read_post = ReadPost.objects.get(user=user, post=post)
        read_post.is_read = True
        read_post.save()
        return Response({"detail": "Post marked as read."})

from rest_framework import generics
from blog.models import User, Post
from .serializers import UserSerializer, PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.order_by("-created")
    serializer_class = PostSerializer

from rest_framework import serializers
from django.contrib.auth.models import User

from blog.models import Blog, Post, Subscriptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions

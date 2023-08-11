from rest_framework import serializers
from django.contrib.auth.models import User
from django.template.defaultfilters import (
    date as date_filter,
    time as time_filter,
)

from blog.models import Blog, Post, Subscriptions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"



class PostSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = "__all__"

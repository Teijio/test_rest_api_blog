from rest_framework import serializers
from django.contrib.auth.models import User


from blog.models import Blog, Post, Subscriptions, ReadPost


class UserSerializer(serializers.ModelSerializer):
    is_follow = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", "is_follow")

    def get_is_follow(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            user = request.user
            return Subscriptions.objects.filter(
                user=user, blog=obj.blog
            ).exists()
        return False


class ReadPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadPost
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    is_read = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_is_read(self, obj):
        user = self.context.get("request").user
        read_post = ReadPost.objects.filter(user=user, post=obj).first()
        if read_post:
            return read_post.is_read
        return False


class PostSubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = "__all__"

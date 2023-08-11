from celery import shared_task
from django.contrib.auth.models import User
from django.conf import settings

from .models import Post


@shared_task
def display_user_feed_posts():
    users = User.objects.all()
    for user in users:
        subscribed_blogs = user.user_subscriptions.all().values_list("blog")
        posts = Post.objects.filter(blog__in=subscribed_blogs).order_by(
            "-created"
        )[:settings.LAST_POSTS]

        print(f"User: {user.username}")
        for post in posts:
            print(f"Post Title: {post.title}")

from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.username} blog"


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=140, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.title


class Subscriptions(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_subscriptions",
        verbose_name="User",
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="blog_subscriptions",
        verbose_name="Blog",
    )

    class Meta:
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "blog"),
                name="unique_subscriptions",
            )
        ]

    def __str__(self):
        return f"{self.user} subscribed to {self.blog}"


class ReadPost(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="read_posts",
        verbose_name="User",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="read_posts_by_user",
        verbose_name="Post",
    )
    is_read = models.BooleanField(default=False, verbose_name="Is Read")

    class Meta:
        verbose_name = "Readpost"
        verbose_name_plural = "Readposts"
        constraints = [
            models.UniqueConstraint(
                fields=("user", "post"), name="unique_posts"
            )
        ]

    def __str__(self):
        return f"{self.user} is read {self.post}"

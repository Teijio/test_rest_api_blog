from django.contrib import admin

from .forms import SubscriptionsForm
from .models import Blog, Post, Subscriptions


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["owner"]


@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    form = SubscriptionsForm
    list_display = ["user", "blog"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "blog", "created"]
    list_filter = ["created", "blog"]
    search_fields = ["title"]

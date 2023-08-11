from django.urls import include, path
from rest_framework import routers

from .views import (
    BlogPostViewSet,
    PostSubscriptionsViewSet,
    UserListView,
)

router = routers.DefaultRouter()
router.register(
    r"blog_posts",
    BlogPostViewSet,
    basename="blog_posts",
)
router.register(
    r"users",
    UserListView,
    basename="users",
)
router.register(
    r"post_subscriptions",
    PostSubscriptionsViewSet,
    basename="post_subscriptions",
)


urlpatterns = [
    path("", include(router.urls)),
]

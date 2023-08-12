import os
from tqdm import tqdm
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from mixer.backend.django import mixer
from django.contrib.auth.models import User

from blog.models import Post, Subscriptions

USERS = 20
POSTS = 10

users = mixer.cycle(USERS).blend(User)


for user in tqdm(users, desc="Creating posts"):
    mixer.cycle(POSTS).blend(Post, blog=user.blog)


for i in tqdm(range(1, len(users) // 2), desc="Creating subscriptions"):
    mixer.blend(Subscriptions, user=users[i], blog=users[-i].blog)
    mixer.blend(Subscriptions, user=users[i], blog=users[-i-1].blog)

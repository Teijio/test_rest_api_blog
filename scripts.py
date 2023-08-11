import os
from tqdm import tqdm
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from mixer.backend.django import mixer
from django.contrib.auth.models import User

from blog.models import Post, Subscriptions


users = list(tqdm(mixer.cycle(100).blend(User), desc="Creating users"))


for user in tqdm(users, desc="Creating posts"):
    mixer.cycle(10).blend(Post, blog=user.blog)


for i in tqdm(range(1, len(users) // 2), desc="Creating subscriptions"):
    mixer.blend(Subscriptions, user=users[i], blog=users[-i].blog)
    mixer.blend(Subscriptions, user=users[i], blog=users[-i-1].blog)

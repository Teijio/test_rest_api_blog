# Generated by Django 3.2.20 on 2023-08-10 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_subscriptions', to='blog.blog', verbose_name='Blog')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddConstraint(
            model_name='subscriptions',
            constraint=models.UniqueConstraint(fields=('user', 'blog'), name='unique_subscriptions'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-created'], name='blog_post_created_76eb4c_idx'),
        ),
    ]

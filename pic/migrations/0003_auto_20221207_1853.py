# Generated by Django 3.2.16 on 2022-12-07 18:53

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pic', '0002_feed_follow_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='feed',
            name='following_accounts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_followed_accounts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pic.post'),
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(default='placeholder', on_delete=django.db.models.deletion.CASCADE, related_name='following_account_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(default='placeholder', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(default='placeholder', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-07 19:51

import cloudinary.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Tag')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('caption', models.CharField(max_length=10000, verbose_name='Caption')),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(related_name='tags', to='pic.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(default='placeholder', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('following', models.ForeignKey(default='placeholder', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('following_accounts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed_followed_accounts', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pic.post')),
                ('user', models.ForeignKey(default='placeholder', on_delete=django.db.models.deletion.CASCADE, related_name='following_account_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
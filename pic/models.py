from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.utils.text import slugify
from django.db.models.signals import post_save, post_delete
import uuid
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True, default=uuid.uuid1)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    picture = CloudinaryField('image', default='placeholder')
    caption = models.CharField(max_length=10000, verbose_name="Caption")
    posted = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="tags")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("post-details", args=[str(self.id)])

    def number_of_likes(self):
        return self.likes.count()


class Likes(models.Model):
    # Likes model to be created here
    def like_post():
        # like post code
        print('Test')

    def unlike_post():
        # unlike post code
        print('Test')


class Follow(models.Model):
    # Delete defaults after DB migration
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    # def follow_account():
    #     # like post code
    #     print('Test')

    # def unfollow_account():
    #     # unlike post code
    #     print('Test')


class Feed(models.Model):
    # Delete defaults after DB migration
    following_accounts = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='feed_followed_accounts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_account_user', default='placeholder')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def add_post(sender, instance, *args, **kwargs):
        # like post code
        post = instance
        user = post.user
        followers = Follow.objects.all().filter(following=user)
        for follower in followers:
            feed = Feed(post=post, user=follower.follower, date=post.posted, following=user)
            feed.save()


post_save.connect(Feed.add_post, sender=Post)

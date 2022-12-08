from django.shortcuts import render
from django.contrib.auth.models import User
from pic.models import Tag, Post, Likes, Follow, Feed
from django.contrib.auth.decorators import login_required


def index(request):
    user = User.objects.get(username=request.user.username)
    feed_posts = Feed.objects.filter(user=user)
    feed_posts_list = []
    for post in feed_posts:
        feed_posts_list.append(post.post_id)
    render_posts = Post.objects.filter(
        id__in=feed_posts_list).all().order_by('-posted')
    context = {
        'render_posts': render_posts,
    }

    return render(request, 'index.html', context)

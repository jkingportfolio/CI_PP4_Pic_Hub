from django.contrib import admin
from pic.models import Tag, Post, Likes, Follow, Feed

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Follow)
admin.site.register(Feed)

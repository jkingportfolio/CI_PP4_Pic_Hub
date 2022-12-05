from django.contrib import admin
from pic.models import Tag, Post

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Follow)
admin.site.register(Feed)

from django.contrib import admin
from pic.models import Tag, Post, Likes, Follow, Feed

# Register your models here.
admin.site.register(Tag)
# admin.site.register(Post)
admin.site.register(Likes)
admin.site.register(Follow)
admin.site.register(Feed)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = (
        'id',
        'picture',
        'caption',
        'posted',
        'user',
        'likes',
    )    

    def get_tags(self, obj): 
        return "\n".join([t.tags for t in obj.tags.all()])


admin.site.register(Post, PostAdmin)

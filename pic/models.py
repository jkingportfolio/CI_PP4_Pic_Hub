from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = CloudinaryField('image', default='placeholder')
    caption = models.CharField(max_length=1000, verbose_name="Caption")
    posted = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="tags")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["-posted"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

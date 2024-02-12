from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE

from blog.utils import avatar_path


# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, AbstractBaseModel):
    avatar = models.ImageField(upload_to=avatar_path)

    @property
    def post_count(self):
        return self.posts.count()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Post(AbstractBaseModel):
    title = models.CharField(max_length=128)
    content = models.TextField()
    published = models.DateField()
    is_active = models.BooleanField(default=False)
    author = models.ForeignKey('blog.User', CASCADE, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

from django.db import models
from django.contrib.auth.models import User
import uuid


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pen_name = models.CharField(max_length=250, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    published_date = models.DateTimeField(auto_now_add=True, editable=False)
    image = models.ImageField(upload_to='images/', null=True)
    snippet = models.CharField(max_length=250)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title
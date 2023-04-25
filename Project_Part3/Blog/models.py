from django.db import models
from django.contrib.auth.models import User

class NewPost(models.Model):
    titulo = models.CharField(max_length=300)
    body = models.CharField(max_length=3000)
    image= models.ImageField(null=True, blank=True, upload_to="post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(NewPost, on_delete=models.CASCADE, related_name="comments")
    titulo = models.CharField(max_length=100)
    body = models.TextField()
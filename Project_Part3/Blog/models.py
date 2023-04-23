from django.db import models

class NewPost(models.Model):
    titulo = models.CharField(max_length=300)
    body = models.CharField(max_length=3000)
    image= models.ImageField(null=True, blank=True, upload_to="post")

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    titulo = models.CharField(max_length=100)
    body = models.TextField()
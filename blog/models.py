from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=40)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + self.author.username

    def get_absolute_url(self):
        return reverse('home')


class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} | {self.post.title} | {self.content}"

    def get_absolute_url(self):
        return reverse('home')


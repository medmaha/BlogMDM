from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone

# Create your models her

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # go to the post deatil url after post complete
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    comment = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comment')
    created = models.DateTimeField(auto_now_add=True)

class ReplyPostComments(models.Model):
    reply = models.TextField(max_length=200, null=True)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies')
    date_send = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


from django.db import models
from django.contrib.auth.models import User
# new
from django.urls import reverse
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    description = models.CharField(max_length=255)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='posts')
    # new
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='posts')
    likes = models.ManyToManyField(User, blank=True, related_name='liked_posts')

    # new
    class Meta:
        # новые посты будут в начале
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    author = models.ForeignKey(User,on_delete=models.CASCADE,
                               related_name='comments')
    content = models.TextField()

    def __str__(self):
        return f'comment on {self.post.title}'

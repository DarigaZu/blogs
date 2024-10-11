from django.db import models
from apps.blogs.models import Blog
from django.contrib.auth.models import User

class Like(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    
    class Meta:
        unique_together = ('blog', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.blog.title}'    
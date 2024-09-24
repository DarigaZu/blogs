from django.db import models
from apps.blogs.models import Blog  
from django.contrib.auth.models import User

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments') 
    text = models.TextField(verbose_name='Comment text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at', null=True)

    def __str__(self):
        return f'Comment on {self.blog}'
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

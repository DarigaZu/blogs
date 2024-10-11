from django.db import models
from apps.blogs.models import Blog  

class Tag(models.Model):
    blogs = models.ManyToManyField(Blog, related_name='tags', verbose_name='блог')  
    title = models.CharField(max_length=100, verbose_name='Tag text') 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'    
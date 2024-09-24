from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(
        max_length=50, 
        verbose_name='Title',
    )

    description = models.TextField(
        verbose_name='Description',
    )

    image = models.ImageField(
        upload_to='blogs/',
        verbose_name='Image',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    create_at = models.DateField(
        auto_now_add=True,
        verbose_name='Create at',
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
from django.shortcuts import render, redirect, get_object_or_404

from apps.likes.models import Like
from apps.blogs.models import Blog


def  like_list(request):
    like = Like.objects.all()
    return render(request, 'likes/like_list.html', {'like': like})

def like_create(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        user = request.user
        Like.objects.get_or_create(blog=blog, user=user) 
        return redirect('like_list')
    return render(request, 'likes/like_create.html', {'blog': blog}) 

def like_update(request, pk):
    like = get_object_or_404(Like, id=pk)
    if request.method == 'POST':
        like.title = request.POST.get('title')
        like.save()
        return redirect('like_list')
    return render(request, 'likes/like_update.html', {'like': like})

def like_delete(request, pk):
    like = get_object_or_404(Like, id=pk)
    if request.method == 'POST':
        like.delete()
        return redirect('like_list')
    return render(request, 'likes/like_delete.html', {'like': like})

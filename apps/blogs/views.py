from django.shortcuts import render, redirect
from django.contrib import messages

from apps.blogs.models import Blog
from apps.comments.models import Comment


def homepage(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', locals())

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        blog_create = Blog.objects.create(author = request.user, title = title, description = description, image = image)
        return redirect('index') 
    
    return render(request, 'blogs/create.html')

def retrieve(request, pk):
    blogs = Blog.objects.get(id=pk)
    if request.method == 'POST':
        if 'comment' in request.POST:
            try:
                text = request.POST['text']
                Comment.objects.create(blog=blogs, text=text)
                return redirect('retrieve', blogs.id)
            except Exception as e:
                messages.error(request, e)
    return render(request, 'blogs/retrieve.html', locals())


def update(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image', blog.image)  

        blog.title = title
        blog.description = description
        blog.image = image
        blog.save()

        return redirect('retrieve', pk=pk) 

    return render(request, 'blogs/update.html', {'blog': blog})


def delete(request, pk):
    if request.method == 'POST':
        blog = Blog.objects.get(id=pk)
        blog.delete()
        return redirect('index')
    
    return render(request, 'blogs/delete.html')





from django.shortcuts import render, redirect, get_object_or_404
from apps.tags.models import Tag

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})

def tag_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Tag.objects.create(title=title)
        return redirect('tag_list')
    return render(request, 'tags/tag_create.html')

def tag_update(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    if request.method == 'POST':
        tag.title = request.POST.get('title')
        tag.save()
        return redirect('tag_list')
    return render(request, 'tags/tag_update.html', {'tag': tag})

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, id=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')
    return render(request, 'tags/tag_delete.html', {'tag': tag})

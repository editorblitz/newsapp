from django.shortcuts import render
from .models import Post, HomepageSection, HomepageSectionOrder

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_create(request):
    # Logic for creating a new post
    pass

def post_edit(request, post_id):
    # Logic for editing an existing post
    pass

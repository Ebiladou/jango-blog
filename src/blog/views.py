from django.shortcuts import render, get_object_or_404
from .models import Blog_post

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def blog_home(request):
    published_posts = Blog_post.objects.filter(status='published').order_by('-created_at')
    
    context = {
        'posts': published_posts,
    }
    return render(request, 'blog/blog_home.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Blog_post, slug=slug, status='published')
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

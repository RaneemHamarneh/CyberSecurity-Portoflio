
# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import BlogPost




def posts_list(request):
    posts = BlogPost.objects.filter(published=True).order_by("-published_at", "-id")
    return render(request, "blog/posts_list.html", {"posts": posts})




def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})
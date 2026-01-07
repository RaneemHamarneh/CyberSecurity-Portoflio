
# Create your views here.
from django.shortcuts import render
from portfolio.models import Project, Certification
from blog.models import BlogPost




def home(request):
    featured_projects = Project.objects.filter(published=True, featured=True)[:4]
    featured_certs = Certification.objects.filter(featured=True)[:4]
    latest_posts = BlogPost.objects.filter(published=True).order_by("-published_at", "-id")[:3]
    return render(request, "core/home.html", {
        "featured_projects": featured_projects,
        "featured_certs": featured_certs,
        "latest_posts": latest_posts,
    })
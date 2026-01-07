from django.contrib import admin

# Register your models here.
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "published_at")
    list_filter = ("published",)
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}
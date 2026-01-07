from django.contrib import admin

# Register your models here.
from .models import Project, Document, Certification


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "role_type", "published", "featured", "updated_at")
    list_filter = ("role_type", "published", "featured")
    search_fields = ("title", "summary", "tools")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "doc_type", "is_redacted_public", "related_project", "updated_at")
    list_filter = ("doc_type", "is_redacted_public")
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "issued_at", "featured")
    list_filter = ("issuer", "featured")
    search_fields = ("name", "issuer")
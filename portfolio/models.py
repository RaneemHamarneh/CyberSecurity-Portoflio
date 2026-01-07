# from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
import bleach


ALLOWED_TAGS = [
    "p", "br", "strong", "em", "ul", "ol", "li",
    "h2", "h3", "blockquote", "code", "pre", "a"
]
ALLOWED_ATTRS = {
    "a": ["href", "title", "target", "rel"],
}


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

class Project(Timestamped):
    ROLE_TYPES = [
    ("SOC", "SOC"),
    ("DFIR", "DFIR"),
    ("SIEM", "SIEM"),
    ("Cloud", "Cloud Security"),
    ("AppSec", "Application Security"),
    ("GRC", "GRC"),
    ]


    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=280)
    role_type = models.CharField(max_length=16, choices=ROLE_TYPES, default="SOC")


    # Use RichTextField but sanitize on save
    problem_statement = RichTextField(blank=True)
    approach = RichTextField(blank=True)
    outcomes = RichTextField(blank=True)


    tools = models.CharField(max_length=300, blank=True, help_text="Comma-separated tools")
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)


    tags = TaggableManager(blank=True)
    def clean_rich(self, value: str) -> str:
        return bleach.clean(
            value or "",
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRS,
            protocols=["http", "https", "mailto"],
            strip=True,
        )


    def save(self, *args, **kwargs):
        self.problem_statement = self.clean_rich(self.problem_statement)
        self.approach = self.clean_rich(self.approach)
        self.outcomes = self.clean_rich(self.outcomes)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return self.title
class Document(Timestamped):
    DOC_TYPES = [
    ("IR", "Incident Report"),
    ("HUNT", "Threat Hunt"),
    ("DETECTION", "Detection Rule"),
    ("PCAP", "PCAP Analysis"),
    ("AUDIT", "Audit Checklist"),
    ("NOTES", "Lab Notes"),
    ]


    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    doc_type = models.CharField(max_length=16, choices=DOC_TYPES)
    summary = models.CharField(max_length=280, blank=True)


    # File uploads (PDF recommended)
    file = models.FileField(upload_to="documents/")

    # Optional: public redacted only
    is_redacted_public = models.BooleanField(default=True)


    related_project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)
    tags = TaggableManager(blank=True)


    def get_absolute_url(self):
        return reverse("document_detail", kwargs={"slug": self.slug})


    def __str__(self):
        return self.title




class Certification(Timestamped):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=120)
    issued_at = models.DateField()
    credential_url = models.URLField(blank=True)


    # Credly embed
    credly_share_badge_id = models.CharField(max_length=64, blank=True)
    credly_host = models.URLField(default="https://www.credly.com", blank=True)


    featured = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} ({self.issuer})"
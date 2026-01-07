
# Create your models here.
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
import bleach

ALLOWED_TAGS = ["p","br","strong","em","ul","ol","li","h2","h3","blockquote","code","pre","a"]
ALLOWED_ATTRS = {"a": ["href","title","target","rel"]}

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=280)
    content = RichTextField()

    published = models.BooleanField(default=True)
    published_at = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.content = bleach.clean(
            self.content or "",
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRS,
            protocols=["http","https","mailto"],
            strip=True,
        )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

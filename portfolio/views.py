from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Project, Document, Certification




def projects_list(request):
    q = request.GET.get("q", "").strip()
    tag = request.GET.get("tag", "").strip()


    qs = Project.objects.filter(published=True).order_by("-featured", "-updated_at")


    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(summary__icontains=q) | Q(tools__icontains=q))


    if tag:
        qs = qs.filter(tags__name__iexact=tag)


    return render(request, "portfolio/projects_list.html", {"projects": qs, "q": q, "tag": tag})




def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, published=True)
    related_docs = Document.objects.filter(related_project=project, is_redacted_public=True)
    return render(request, "portfolio/project_detail.html", {"project": project, "related_docs": related_docs})




def documents_list(request):
    q = request.GET.get("q", "").strip()
    tag = request.GET.get("tag", "").strip()
    qs = Document.objects.filter(is_redacted_public=True).order_by("-updated_at")


    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(summary__icontains=q))


    if tag:
        qs = qs.filter(tags__name__iexact=tag)


    return render(request, "portfolio/documents_list.html", {"documents": qs, "q": q, "tag": tag})




def document_detail(request, slug):
    doc = get_object_or_404(Document, slug=slug, is_redacted_public=True)
    return render(request, "portfolio/document_detail.html", {"doc": doc})




def certifications(request):
    certs = Certification.objects.order_by("-featured", "-issued_at")
    return render(request, "portfolio/certifications.html", {"certifications": certs})
from django.urls import path
from . import views


urlpatterns = [
    path("", views.projects_list, name="projects_list"),
    path("<slug:slug>/", views.project_detail, name="project_detail"),
    path("documents/", views.documents_list, name="documents_list"),
    path("documents/<slug:slug>/", views.document_detail, name="document_detail"),
    path("certifications/", views.certifications, name="certifications"),
    ]
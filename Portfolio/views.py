from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImages

# Create your views here.
def portfolioPage(request):
    projects = Project.objects.all().order_by('-date')
    return render(request, 'pages/portfolio.html', {"projects": projects})


def EachPage(request, slug):
    project = get_object_or_404(Project, slug=slug)
    gallery_list = ProjectImages.objects.filter(project=project)
    return render(request, 'pages/portfolioPage.html', {"page": project, "gallery_list": gallery_list})
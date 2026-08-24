from django.shortcuts import render
from Portfolio.models import Project

def homePage(request):
    latest_projects = Project.objects.order_by('-date')[:5]
    return render(request, 'index.html', {"latest_projects" : latest_projects})

def servicesPage(request):
    return render(request, 'services.html')

def portfolioPage(request):
    return render(request, 'pages/portfolio.html')

def aboutPage(request):
    return render(request, 'about.html')

def contactsPage(request):
    return render(request, 'contacts.html')
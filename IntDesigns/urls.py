"""
URL configuration for IntDesigns project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.views.static import serve
from . import views
from Contacts.views import contactsPage as contacts_view, consultationPage as consultation_view, appointmentPage as appointment_view
from django.conf import settings

urlpatterns = [
    path('', views.homePage, name='home'),
    path('services/', views.servicesPage, name='services'),
    path('about/', views.aboutPage, name='about'),

    path('contacts/', contacts_view, name='contacts'),
    path('appointment/', appointment_view, name='appointment'),
    path('consultation/', consultation_view, name='consultation'),
    path('portfolio/', include(('Portfolio.urls', 'portfolio'), namespace='portfolio')),
    path('dashboard/', include('Dashboard.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
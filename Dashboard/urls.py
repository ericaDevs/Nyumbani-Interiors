from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.login_user, name = "login"),
    path('logout/', views.logout_user, name = 'logout'),
    path('overview/', views.overview, name='overview'),
    path('projects/', views.addProject, name="projects"),
    path('appointments/', views.appointments, name="appointments"),
    path('consultation/', views.consultation, name="consultation"),
    path('contacts/', views.contacts, name="contacts"),
    path('deleteProject/<slug:slug>/', views.deleteProject, name="deleteProject"),
    path('editProject/<slug:slug>/', views.editProject, name="editProject"),
    path('deleteAppointment/<int:id>/', views.deleteAppointment, name="deleteAppointment"),
    path('deleteConsultation/<int:id>/', views.deleteConsultation, name="deleteConsultation"),
    path('deleteContact/<int:id>/', views.deleteContact, name="deleteContact"),
]

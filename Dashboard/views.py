from django.shortcuts import render, get_object_or_404, redirect
from Portfolio.models import Project, ProjectImages
from Contacts.models import Contacts, Appointments, Consultation
from Portfolio.forms import CreateNewProject
from django.contrib import messages
from django.utils.text import slugify
from Dashboard.forms import UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import os


# ADMIN AUTHORIZATION & AUTHENTICATION
def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard:overview')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Please fill in all fields!")
            return render(request, "base/login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('dashboard:overview')
        messages.error(request, "Invalid username or password, please check your credentials and try again!")
        return render(request, "base/login.html")
    
    return render(request, 'base/login.html')


# LOGOUT
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('dashboard:login')



# ADMIN DASHBOARD
@login_required
def overview(request):
    projects = Project.objects.all()
    total_projects = projects.count()
    appointments = Appointments.objects.all().count()
    consultations = Consultation.objects.all().count()
    contacts = Contacts.objects.all().count()

    # include an empty form so the dashboard modal renders fields
    form = CreateNewProject()

    context = {
        "projects": projects,
        "total_projects": total_projects,
        "total_appointments": appointments,
        "total_consultation": consultations,
        "contacts": contacts,
        "form": form,
    }

    return render(request, 'base/overview.html', context)


# ADD NEW PROJECTS
@login_required
def addProject(request):
    if request.method == "POST":
        form = CreateNewProject(request.POST, request.FILES)
        gallery_list = request.FILES.getlist('gallery_images')
        if len(gallery_list) > 5:
            messages.error(request, "You can upload a maximum of five gallery images")
            return redirect('dashboard:projects')
        elif form.is_valid():
            # create instance without saving so we can set a unique slug
            project = form.save(commit=False)

            # generate slug from title if not provided and ensure uniqueness
            if not project.slug:
                base_slug = slugify(project.title)
                slug = base_slug
                counter = 1
                while Project.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                project.slug = slug

            project.save()
            for f in gallery_list[:5]:
                ProjectImages.objects.create(project=project, images=f)
            messages.success(request, "Project Added successfully!")
            return redirect('dashboard:projects')
        else:
            messages.error(request, "An error occured, please check your form and submit again!")

    else:
        form = CreateNewProject()
    # Collect analytics same as adminDashboard so dashboard isn't empty
    projects = Project.objects.all().order_by('-date')
    total_projects = projects.count()
    appointments = Appointments.objects.all().count()
    consultations = Consultation.objects.all().count()
    contacts = Contacts.objects.all().count()

    context = {
    "projects": projects,
    "total_projects": total_projects,
    "total_appointments": appointments,
    "total_consultation": consultations,
    "contacts": contacts,
    "form": form
    }

    return render(request, 'base/portfolio.html', context)


# EDIT PROJECT
@login_required
def editProject(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        form = CreateNewProject(request.POST, request.FILES, instance=project)
        gallery_list = request.FILES.getlist('gallery_images')
        if len(gallery_list) > 5:
            messages.error(request, "You can upload a maximum of five gallery images")
            return redirect('dashboard:projects')
        
        if form.is_valid():
            proj = form.save(commit=False)
            # 1. FIX: Update slug if title changed
            new_base_slug = slugify(proj.title)
            if new_base_slug != proj.slug:
                base_slug = new_base_slug
                newSlug = base_slug
                counter = 1
                while Project.objects.exclude(pk=proj.pk).filter(slug=newSlug).exists():
                    newSlug = f"{base_slug}-{counter}"
                    counter += 1
                proj.slug = newSlug
            proj.save()

            if gallery_list:
                ProjectImages.objects.filter(project=proj).delete()
                for f in gallery_list[:5]:
                    ProjectImages.objects.create(project=proj, images=f)

            messages.success(request, 'Project updated successfully.')
            return redirect('dashboard:projects')
        else:
            messages.error(request, 'Please correct the errors and resubmit.')

    else:
        form = CreateNewProject(instance=project)
        gallery_list = ProjectImages.objects.filter(project=project)

    return render(request, 'base/portfolio.html', {'form': form, 'project': project, 'gallery_list': gallery_list})

# delete project
@login_required
def deleteProject(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if request.method == 'POST':
        # Delete associated image files from the filesystem
        if project.main_image and project.main_image.name:
            try:
                if os.path.isfile(project.main_image.path):
                    os.remove(project.main_image.path)
            except Exception:
                pass
        if project.before_image and project.before_image.name:
            try:
                if os.path.isfile(project.before_image.path):
                    os.remove(project.before_image.path)
            except Exception:
                pass
        # Delete gallery images linked to this project
        gallery_images = ProjectImages.objects.filter(project=project)
        for img in gallery_images:
            if img.images and img.images.name:
                try:
                    if os.path.isfile(img.images.path):
                        os.remove(img.images.path)
                except Exception:
                    pass
        # Now delete the project and related ProjectImages records (cascade)
        project.delete()
        messages.success(request, 'Project deleted successfully.')
        return redirect('dashboard:projects')


# APPOINTMENTS
@login_required
def appointments(request):
    appointments = Appointments.objects.all().order_by('-date')
    total_appointments = appointments.count()
    total_projects= Project.objects.count()
    consultations = Consultation.objects.all().count()
    contacts = Contacts.objects.all().count()

    context = {
    "appointments": appointments,
    "total_projects": total_projects,
    "total_appointments": total_appointments,
    "total_consultation": consultations,
    "contacts": contacts
    }

    return render(request, 'base/appointment.html', context)



# CONSULTATIONS
@login_required
def consultation(request):
    consultations = Consultation.objects.all().order_by('-id')
    total_consultations = consultations.count()
    total_projects = Project.objects.all().count()
    appointments = Appointments.objects.all().count()
    contacts = Contacts.objects.all().count()

    context = {
    "consultations": consultations,
    "total_consultations": total_consultations,
    "total_appointments": appointments,
    "total_projects": total_projects,
    "contacts": contacts
    }

    return render(request, 'base/consultation.html', context)



# CONTACTS & INQUIRIES
@login_required
def contacts(request):
    contacts = Contacts.objects.all().order_by('-id')
    total_contacts = contacts.count()
    total_projects = Project.objects.all().count()
    appointments = Appointments.objects.all().count()
    consultations = Consultation.objects.all().count()

    context = {
        "contacts": contacts,
        "total_contacts": total_contacts,
        "total_projects": total_projects,
        "total_appointments": appointments,
        "total_consultation": consultations
    }

    return render(request, 'base/contacts.html', context)



# DELETE APPOINTMENT
@login_required
def deleteAppointment(request, id):
    appointment = get_object_or_404(Appointments, id=id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully.')
    return redirect('dashboard:appointments')



# DELETE CONSULTATION
@login_required
def deleteConsultation(request, id):
    consultation = get_object_or_404(Consultation, id=id)
    if request.method == 'POST':
        consultation.delete()
        messages.success(request, 'Consultation deleted successfully.')
    return redirect('dashboard:consultation')



# DELETE CONTACT
@login_required
def deleteContact(request, id):
    contact = get_object_or_404(Contacts, id=id)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact inquiry deleted successfully.')
    return redirect('dashboard:contacts')

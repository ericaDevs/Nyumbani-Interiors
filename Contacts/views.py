from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ContactsForm, ConsultationForm, AppointmentsForm

# Create your views here.
def contactsPage(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contacts')
        messages.error(request, "There was an error with your submission. Please check the form and try again.")
        return redirect('contacts')
    form = ContactsForm()
    return render(request, 'pages/contacts.html', {"form" : form})


def consultationPage(request):
    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your consultation request has been received successfully.")
            return redirect('consultation')
        messages.error(request, "There was an error with your submission. Please check the form and try again.")
        return redirect('consultation')
    form = ConsultationForm()
    return render(request, 'pages/consultation.html', {"form" : form})


def appointmentPage(request):
    if request.method == "POST":
        form = AppointmentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your appointment has been scheduled successfully.")
            return redirect('appointment')
        messages.error(request, "There was an error with your submission. Please check the form and try again.")
        return redirect('appointment')
    form = AppointmentsForm()
    return render(request, 'pages/appointment.html', {"form" : form})
from django import forms
from . import models

class ContactsForm(forms.ModelForm):
    class Meta:
        model = models.Contacts
        fields = '__all__'


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = models.Consultation
        fields = '__all__'
        widgets = {
            'preference': forms.RadioSelect(),
            'property_type': forms.Select(),
            'budget': forms.Select(),
        }


class AppointmentsForm(forms.ModelForm):
    class Meta:
        model = models.Appointments
        fields = '__all__'



class ViewAppointment(forms.ModelForm):
    class Meta:
        model = models.Appointments
        fields = '__all__'



        # ['type', 'date','time', 'name',  'phone_number','email','message',]
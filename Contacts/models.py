from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    subject = models.CharField(max_length = 255)
    message = models.TextField()


class Consultation(models.Model):
    property_choices = [
        ("Residential Villa / Home", "Residential Villa / Home"),
        ("Commercial / Office Space", "Commercial / Office Space"),
        ("Hospitality / Restaurant", "Hospitality / Restaurant"),
        ("Retail Storefront", "Retail Storefront")
    ]
    budget_choices = [
        ("Under $10,000", "Under $10,000"),
        ("$10,000 - $30,000", "$10,000 - $30,000"),
        ("$30,000 - $75,000", "$30,000 - $75,000"),
        ("$75,000+", "$75,000+")
    ]

    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    property_type = models.CharField(max_length = 255, choices=property_choices)
    budget = models.CharField(max_length = 255, choices=budget_choices)
    preference = models.CharField(max_length = 255, choices=[
        ("In-Studio (Nairobi)", "In-Studio (Nairobi)"), 
        ("Virtual / Online", "Virtual / Online")
    ])
    message = models.TextField()





class Appointments(models.Model):
    type = models.CharField(max_length = 255)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    message = models.TextField()
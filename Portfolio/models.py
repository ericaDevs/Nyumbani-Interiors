from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True, null=True)
    CATEGORY_CHOICES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial / Office'),
        ('hospitality', 'Hospitality & Restaurants'),
        ('retail', 'Retail & Showrooms'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    client_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=150, default="Nairobi, Kenya")
    completion_year = models.IntegerField(blank=True, null=True)
    main_image = models.ImageField(upload_to='portfolio/covers/')
    before_image = models.ImageField(upload_to='portfolio/before/', blank=True, null=True)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title


#To handle multiple images
class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    images = models.ImageField(upload_to = 'portfolio/gallery')
    caption = models.CharField(max_length = 200)

    def __str__(self):
        return(f"{self.project.title} - Gallery Image")

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
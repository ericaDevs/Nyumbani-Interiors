from django.contrib import admin
from Portfolio.models import Project, ProjectImages

class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages
    extra = 5

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImagesInline]
    list_display = ('title', 'category', 'completion_year')

# Register your models here.
# admin.site.register(ProjectImages)

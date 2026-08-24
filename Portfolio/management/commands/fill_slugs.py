from django.core.management.base import BaseCommand
from django.apps import apps
from django.utils.text import slugify
from django.db.models import Q

class Command(BaseCommand):
    help = "Populate missing/empty slugs for Project objects"

    def handle(self, *args, **options):
        Project = apps.get_model('Portfolio', 'Project')
        qs = Project.objects.filter(Q(slug__isnull=True) | Q(slug=''))
        total = qs.count()
        if total == 0:
            self.stdout.write(self.style.SUCCESS("No projects with empty slugs found."))
            return

        updated = 0
        for project in qs:
            base = slugify(project.title) or f"project-{project.pk}"
            candidate = base
            i = 1
            while Project.objects.exclude(pk=project.pk).filter(slug=candidate).exists():
                candidate = f"{base}-{i}"
                i += 1
            project.slug = candidate
            project.save(update_fields=['slug'])
            updated += 1
            self.stdout.write(f"Updated: id={project.pk} slug={project.slug}")

        self.stdout.write(self.style.SUCCESS(f"Done. {updated} of {total} projects updated."))
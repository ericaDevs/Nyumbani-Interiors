import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Creates or updates an admin superuser using env vars or arguments"

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, default=os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'))
        parser.add_argument('--email', type=str, default=os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@nyumbani.com'))
        parser.add_argument('--password', type=str, default=os.environ.get('DJANGO_SUPERUSER_PASSWORD', ''))

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        if not password:
            self.stdout.write(self.style.WARNING("No password provided (set DJANGO_SUPERUSER_PASSWORD or use --password)."))
            return

        user, created = User.objects.get_or_create(username=username, defaults={'email': email, 'is_staff': True, 'is_superuser': True})
        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created successfully!"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' password updated successfully!"))

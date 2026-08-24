import os
from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'Dashboard'

    def ready(self):
        # Auto-create or sync superuser on app startup when env vars are present
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', '').strip()
        if not password:
            return

        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin').strip()
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@nyumbani.com').strip()

        try:
            from django.contrib.auth import get_user_model
            from django.db import connection

            # Ensure tables are ready before querying
            existing_tables = connection.introspection.table_names()
            if 'auth_user' in existing_tables:
                User = get_user_model()
                user, created = User.objects.get_or_create(
                    username=username,
                    defaults={'email': email, 'is_staff': True, 'is_superuser': True}
                )
                user.email = email
                user.is_staff = True
                user.is_superuser = True
                user.set_password(password)
                user.save()
        except Exception:
            pass

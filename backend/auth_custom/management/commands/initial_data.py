"""
Python Script to load initial data into the database
"""

from django.core.management.base import BaseCommand
from auth_custom.models import User


class Command(BaseCommand):
    help = 'Load initial data into the database'

    def handle(self, *args, **kwargs):
        self.user()

    def user(self):
        """SuperAdmin add"""

        check_user = User.objects.filter(email='admin@admin.com')
        if not check_user:
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin'
            )
            self.stdout.write("Superuser created", ending="")

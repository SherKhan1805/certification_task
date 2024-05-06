import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда для создания пользователя
    """
    def handle(self, *args, **options):
        user = User.objects.create(
            email='superadmin@sky.pro',
            name='superadmin',
            surname='superadmin',
            is_staff=True,
            is_superuser=True

        )

        user.set_password(os.getenv('CSU_PASSWORD'))
        user.save()

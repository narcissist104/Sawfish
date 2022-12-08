from django.core.management.base import BaseCommand, CommandError
from lessons.models import User, Request


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.filter(is_staff=False, is_superuser=False).delete()
        Request.objects.filter().delete()

        print("TO DO: Create an unseed command following the instructions of the assignment carefully.")

from django.core.management.base import BaseCommand, CommandError
from faker import Faker 
from lessons.models import User
from django.db import IntegrityError


class Command(BaseCommand):
    PASSWORD = "Password123"
    COUNT = 100

    def __init__(self):
       super().__init__()
       self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        """Default users: """
        User.objects.create_user(
            "@johndoe",
            first_name="John",
            last_name="Doe",
            email="john.doe@example.org",
            password="Password123",
            bio="bio",
            type="student"
        )
        User.objects.create_user(
            "@petrapickles",
            first_name="Petra",
            last_name="Pickles",
            email="petra.pickles@example.org",
            password="Password123",
            bio="bio",
            type="admin"
        )
        User.objects.create_user(
            "@martymajor",
            first_name="Marty",
            last_name="Major",
            email="marty.major@example.org",
            password="Password123",
            bio="bio",
            type="director"
        )
        user_count = 0
        while user_count < Command.COUNT:
            print(f'Seeding user {user_count}',  end='\r')
            try:
                self._create_user()
            except (IntegrityError):
                continue
            user_count += 1
        print('User seeding complete')
        
    def _create_user(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self._email(first_name, last_name)
        username = self._username(first_name, last_name)
        bio = self.faker.text(max_nb_chars=520)
        User.objects.create_user(
            username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=Command.PASSWORD,
            bio=bio
        )

    def _email(self, first_name, last_name):
        email = f'{first_name}.{last_name}@example.org'
        return email

    def _username(self, first_name, last_name):
        username = f'@{first_name}{last_name}'
        return username

    
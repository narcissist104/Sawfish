from django.core.management.base import BaseCommand, CommandError
from faker import Faker 
from lessons.models import User, Request, Teacher
from django.db import IntegrityError
import datetime, random


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
                self._create_teacher()
            except (IntegrityError):
                continue
            user_count += 1
        print('User seeding complete')
        
    def _create_request(self, user):
        for i in range(50):
            student_id = user.id
            instrument = self.faker.instrument()
            availability = datetime.date(random.randint(2022, 2023), random.randint(1, 12), random.randint(1, 28))
            number_of_lessons = random.randint(1, 5)
            interval = random.randint(1, 5)
            duration = random.randint(1, 5)
            teacher_id = random.randint(1, self.COUNT)
            new_request = Request.objects.create(
                student_id,
                instrument,
                availability,
                number_of_lessons,
                interval,
                duration,
                teacher_id
            )
            new_request.save()

    def _create_user(self):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self._email(first_name, last_name)
        username = self._username(first_name, last_name)
        bio = self.faker.text(max_nb_chars=520)
        new_user = User.objects.create_user(
            username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=Command.PASSWORD,
            bio=bio
        )
        self._create_request(new_user)

    def _create_teacher(self):
        name = self.faker.name()
        new_teacher = Teacher.objects.create_user(
            name,
        )
        new_teacher.save()

    def _email(self, first_name, last_name):
        email = f'{first_name}.{last_name}@example.org'
        return email

    def _username(self, first_name, last_name):
        username = f'@{first_name}{last_name}'
        return username
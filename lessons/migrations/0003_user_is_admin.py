# Generated by Django 4.1.3 on 2022-12-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_rename_title_lesson_teacher_remove_lesson_student_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]

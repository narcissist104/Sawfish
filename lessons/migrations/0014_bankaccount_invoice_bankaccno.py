# Generated by Django 4.1.3 on 2022-11-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0013_request_rename_lessons_lesson_delete_requests_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='bankAccNo',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]

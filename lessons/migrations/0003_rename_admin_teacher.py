# Generated by Django 4.1.2 on 2022-11-18 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_admin_director_invoice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Teacher',
        ),
    ]

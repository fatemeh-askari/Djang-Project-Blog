# Generated by Django 4.2.1 on 2024-03-09 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_projects_alter_contactus_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]

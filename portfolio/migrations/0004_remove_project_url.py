# Generated by Django 4.2.7 on 2023-12-17 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
    ]

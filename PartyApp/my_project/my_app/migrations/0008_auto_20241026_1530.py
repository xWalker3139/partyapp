# Generated by Django 3.1.5 on 2024-10-26 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20241026_1515'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='task',
            name='event',
        ),
        migrations.DeleteModel(
            name='CompleteTask',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]

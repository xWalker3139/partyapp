# Generated by Django 3.1.5 on 2024-10-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20241026_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
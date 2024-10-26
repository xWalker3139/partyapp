# Generated by Django 3.1.5 on 2024-10-26 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_remove_completetask_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='completetask',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='my_app.task'),
        ),
        migrations.AlterField(
            model_name='completetask',
            name='complete',
            field=models.CharField(choices=[('NOT STARTED', 'NOT STARTED'), ('IN PROGRESS', 'IN PROGRESS'), ('FINISH', 'FINISH')], max_length=256, null=True),
        ),
    ]

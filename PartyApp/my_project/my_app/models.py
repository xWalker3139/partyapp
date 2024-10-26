from django.db import models
from django.contrib.auth.models import User

SELECT = (
    ('NOT STARTED', 'NOT STARTED'),
    ('IN PROGRESS', 'IN PROGRESS'),
    ('FINISH', 'FINISH'),
)

class Evenimente(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField()
    title = models.CharField(max_length = 256, null = True, blank = False)
    description = models.CharField(max_length = 10000, null = True, blank = False)
    budget = models.DecimalField(max_digits = 10, decimal_places=2, null=True)
    location = models.CharField(max_length = 256, null = True, blank = False)
    number_of_people = models.IntegerField(null=True, blank=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    event = models.ForeignKey(Evenimente, on_delete=models.CASCADE)
    name = models.CharField(max_length = 256, null = True, blank = False)
    budget = models.DecimalField(max_digits = 10, decimal_places=2, null=True)
    assigned_to = models.CharField(max_length=256, null=True, blank=False)

    def __str__(self):
        return self.name

class CompleteTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    complete = models.CharField(max_length = 256, null = True, blank = False, choices=SELECT)

    def __str__(self):
        return self.complete

class Join(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Evenimente, on_delete=models.CASCADE, related_name="joins")

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} joined {self.event.title}"

# Create your models here.

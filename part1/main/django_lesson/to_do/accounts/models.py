from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # reverse relation

    image = models.ImageField(upload_to='profiles', null=True, blank=True)

    tasks_count = models.IntegerField(default=0)
    in_progress_task_count = models.IntegerField(default=0)
    done_task_count = models.IntegerField(default=0)
    deleted_task_count = models.IntegerField(default=0)

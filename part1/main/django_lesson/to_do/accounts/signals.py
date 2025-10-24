from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from tasks.models import Task


@receiver(post_save, sender=Task)
def add_tasks_count(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user_profile = user.profile

        user_profile.tasks_count += 1
        user_profile.save()


@receiver(pre_delete, sender=Task)
def add_deleted_tasks_count(sender, instance, **kwargs):
    user = instance.user
    user_profile = user.profile

    user_profile.deleted_task_count += 1
    user_profile.save()


@receiver(post_save, sender=Task)
def add_tasks_count(sender, instance, created, **kwargs):
    user = instance.user
    user_profile = user.profile

    if instance.status == 'D':
        user_profile.done_task_count += 1
    elif instance.status == 'I':
        user_profile.in_progress_task_count += 1
    user_profile.save()

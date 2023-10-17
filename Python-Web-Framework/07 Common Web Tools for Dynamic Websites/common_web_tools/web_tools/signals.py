from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from common_web_tools_lab.web_tools.models import Task
from django.contrib.auth.signals import Signal

UserModel = get_user_model()


@receiver(pre_save, sender=Task)
def task_to_be_created(*args, **kwargs):
    ...


@receiver(post_save, sender=Task)
def task_crated(*args, **kwargs):
    ...


@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        ...

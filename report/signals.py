from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Form, FileUpload
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_fileupload(sender, instance, created, **kwargs):
    if created:
        Form.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_fileupload(sender, instance, **kwargs):
    instance.report.save()

@receiver(post_save, sender=User)
def create_fileupload(sender, instance, created, **kwargs):
    if created:
        FileUpload.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_fileupload(sender, instance, **kwargs):
    instance.fileupload.save()
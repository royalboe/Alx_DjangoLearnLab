from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    # if created:
    #     if instance.is_superuser:
    #         UserProfile.objects.create(user=instance, role='ADMIN')
    #     else:
    #         UserProfile.objects.create(user=instance)
    if created:
        role = 'ADMIN' if instance.is_superuser else 'MEMBER'
        UserProfile.objects.get_or_create(user=instance, defaults={'role': role})
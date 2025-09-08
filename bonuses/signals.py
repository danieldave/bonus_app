from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Bonus

@receiver(post_save, sender=User)
def create_user_bonus(sender, instance, created, **kwargs):
    if created:
        Bonus.objects.create(user=instance, bonus_type="WELCOME", amount=100.00)

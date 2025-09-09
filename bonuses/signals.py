# bonuses/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Bonus

@receiver(post_save, sender=User)
def create_user_bonus(sender, instance, created, **kwargs):
    if created:
        # Give a default welcome bonus when a user is created
        Bonus.objects.create(
            user=instance,
            amount=100.00,        # ✅ works with new model
            reason="Welcome Bonus",
            status="approved"     # or keep as "pending" if you want admin approval
        )

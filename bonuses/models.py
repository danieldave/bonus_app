from django.db import models
from django.contrib.auth.models import User

class Bonus(models.Model):
    BONUS_TYPES = [
        ('WELCOME', 'Welcome Bonus'),
        ('REFERRAL', 'Referral Bonus'),
        ('LOYALTY', 'Loyalty Bonus'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    bonus_type = models.CharField(max_length=20, choices=BONUS_TYPES, default='WELCOME')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=100.00)  # default = 100 bonus
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.bonus_type} ({self.amount})"

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Subscription(models.Model):
    SUBSCRIPTION_CHOICES = [
        ('monthly', 'Monthly'),
        ('semi_annual', 'Semi-Annual'),
        ('annual', 'Annual'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=20, choices=SUBSCRIPTION_CHOICES)
    is_active = models.BooleanField(default=False)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Subscription(user={self.user.username}, subscription_type={self.subscription_type}, is_active={self.is_active})"

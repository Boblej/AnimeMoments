from django.contrib.auth.models import User
from django.db import models


class PaymentStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_payment_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"PaymentStatus(user={self.user.username}, is_payment_complete={self.is_payment_complete})"
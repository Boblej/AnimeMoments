from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    avatar = models.ImageField(upload_to='avatars/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
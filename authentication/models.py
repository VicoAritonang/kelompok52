from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = [
        ('restaurant', 'Restaurant'),
        ('buyer', 'Buyer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the built-in User model
    name = models.CharField(max_length=100)
    profile_picture = models.URLField(max_length=500)  # Store the image URL
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"

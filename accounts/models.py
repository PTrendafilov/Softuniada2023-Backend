from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Profile(AbstractUser):    
    ROLE_CHOICES = (
        ('freelancer', 'Freelancer'),
        ('client', 'Client'),
        ('teamleader', 'Team Leader'),
    )
    email = models.EmailField(unique=True)
    points = models.IntegerField(default=0)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='freelancer')
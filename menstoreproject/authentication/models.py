from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES,
        blank=True, null=True)

    def __str__(self):
        return self.email

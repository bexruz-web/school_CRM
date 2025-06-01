from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('leadership', 'Rahbariyat'),
        ('teacher', 'O\'qituvchi'),
        ('staff', 'Maktab jamoasi')
    )
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='teacher')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()}"



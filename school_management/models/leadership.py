from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class LeaderShip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    position = models.CharField(max_length=100, null=False, blank=False, verbose_name='Lavozim')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Telefon raqam')
    photo = models.ImageField(upload_to='leadership_photos/', null=True, blank=True, verbose_name='Rasm')
    bio = models.TextField(verbose_name='Biografiya')
    hired_date = models.DateField(verbose_name='Ishga olingan sana')

    class Meta:
        verbose_name = "Rahbar"
        verbose_name_plural = "Rahbarlar"

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.position}'


class SchoolStaff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Xodim")
    position = models.CharField(max_length=100, null=False, blank=False, verbose_name='Lavozim')
    phone_number = models.CharField(max_length=15, unique=True, verbose_name='Telefon raqam')
    photo = models.ImageField(upload_to='teacher_photos/', null=True, blank=True, verbose_name='Rasm')
    hired_date = models.DateField(verbose_name='Ishga olingan sana')

    class Meta:
        verbose_name = "Maktab xodimi"
        verbose_name_plural = "Maktab xodimlari"

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.position}'

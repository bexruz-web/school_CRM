from django.db import models
from .staff import Teacher, Subject


class Schedule(models.Model):
    WEEKDAY = [
        ("monday", "Dushanba"),
        ("tuesday", "Seshanba"),
        ("wednesday", "Chorshanba"),
        ("thursday", "Payshanba"),
        ("friday", "Juma"),
        ("saturday", "Shanba"),
    ]

    SHIFT_CHOICES = [
        (1, 'Birinchi navbat'),
        (2, 'Ikkinchi navbat'),
    ]

    grade = models.CharField(max_length=10, verbose_name='Sinf')
    shift = models.IntegerField(choices=SHIFT_CHOICES, default=1, verbose_name='Smena')
    subjects = models.ManyToManyField(Subject, related_name="schedules", verbose_name='Fan')
    weekday = models.CharField(max_length=10, choices=WEEKDAY, verbose_name='Hafta kuni')

    class Meta:
        verbose_name = "Dars jadvali"
        verbose_name_plural = "Dars jadvallari"

    def __str__(self):
        return f"{self.grade}-sinf uchun {self.weekday} kungi fanlar "


class BellSchedule(models.Model):
    SHIFT_CHOICES = [
        (1, 'Birinchi navbat'),
        (2, 'Ikkinchi navbat'),
    ]

    shift = models.IntegerField(choices=SHIFT_CHOICES, default=1, verbose_name='Smena')
    start_time = models.TimeField(verbose_name='Boshlanish vaqti')
    end_time = models.TimeField(verbose_name='Tugash vaqti')
    break_time = models.CharField(max_length=20, default='5 daqiqa', verbose_name="Tanaffus vaqti")

    class Meta:
        verbose_name = "Dars jadvali vaqti"
        verbose_name_plural = "Dars jadvali vaqtlari"

    def __str__(self):
        return f"{self.get_shift_display()} | {self.start_time} - {self.end_time} | {self.break_time} tanaffus"

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="O'qituvchi")
    phone_number = models.CharField(max_length=13, verbose_name="Telefon raqami")
    photo = models.ImageField(upload_to="teacher_photos/", verbose_name="Rasm")
    bio = models.TextField(verbose_name="Ma'lumotnoma")
    hired_date = models.DateField(verbose_name="Qabul qilingan sana")

    class Meta:
        verbose_name = "O'qituvchi"
        verbose_name_plural = "O'qituvchilar"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=55, verbose_name="Fan nomi")

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

    def __str__(self):
        return self.name


class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Fan")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="O'qituvchi")

    class Meta:
        unique_together = ('subject', 'teacher')
        verbose_name = "Fan-O'qituvchi"
        verbose_name_plural = "Fan-O'qituvchilar"

    def __str__(self):
        return f"{self.teacher.user.first_name} {self.teacher.user.last_name} - {self.subject.name}"


class Student(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Ism-sharifi")
    grade = models.IntegerField(verbose_name="Sinf")
    birth_date = models.DateField(max_length=20, verbose_name="Tug'ilgan sanasi")
    phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name="Telefon raqami")

    class Meta:
        verbose_name = "O'quvchi"
        verbose_name_plural = "O'quvchilar"

    def __str__(self):
        return f"{self.grade}-sinf o'quvchisi {self.full_name}"

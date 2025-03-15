from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="O'qituvchi")
    phone_number = models.CharField(max_length=13, verbose_name="Telefon raqami")
    photo = models.ImageField(upload_to="teachers/", verbose_name="Rasm")
    bio = models.TextField(verbose_name="Ma'lumotnoma")
    hired_date = models.DateTimeField(verbose_name="Qabul qilingan sana")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Subject(models.Model):
    name = models.CharField(max_length=55, verbose_name="Fan nomi")

    def __str__(self):
        return self.name


class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Fan")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="O'qituvchi")

    class Meta:
        unique_together = ('subject', 'teacher')

    def __str__(self):
        return f"{self.teacher.user.first_name} {self.teacher.user.last_name} - {self.subject.name}"


class Student(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="Ism-sharifi")
    grade = models.IntegerField(verbose_name="Sinf")
    birth_date = models.CharField(max_length=20, verbose_name="Tug'ilgan sanasi")
    phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name="Telefon raqami")

    def __str__(self):
        return f"{self.grade}-sinf o'quvchisi {self.full_name}"

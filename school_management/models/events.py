from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Tadbir nomi')
    date = models.DateField(default=timezone.now, verbose_name='Tadbir sanasi')
    description = models.TextField(verbose_name='Tavsif')

    class Meta:
        verbose_name = "Tadbir"
        verbose_name_plural = "Tadbirlar"

    def __str__(self):
        return self.title


class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_photos', verbose_name='Tadbir')
    photos = models.ImageField(upload_to='event_photos/', verbose_name='Rasm')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Yuklangan vaqt')

    class Meta:
        verbose_name = "Tadbir surati"
        verbose_name_plural = "Tadbir suratlari"

    def __str__(self):
        return f"Rasm {self.id} ({self.event.title})"

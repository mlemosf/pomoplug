import uuid
from datetime import datetime, timezone

from django.db import models
from django.utils import timezone as django_timezone


# Create your models here.
class Pomodoro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return str(self.title)

    @property
    def is_running(self):
        if self.end_time is None:
            return True
        current_time = django_timezone.now()
        return current_time < self.end_time

    @property
    def time_left(self):
        if self.end_time is None:
            return "Pomodoro not running"
        current_time = django_timezone.now()
        remaining_time = (self.end_time - current_time).total_seconds()
        minutes, seconds = divmod(remaining_time, 60)
        return f"{minutes}:{seconds:02d}"

    @property
    def elapsed_time(self):
        if self.start_time is None:
            return "Pomodoro not started"
        current_time = django_timezone.now()
        elapsed_time = (current_time - self.start_time).total_seconds()
        minutes, seconds = divmod(elapsed_time, 60)
        return f"{minutes}:{seconds:02d}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.start_time = django_timezone.now()
        super().save(*args, **kwargs)

import uuid
from datetime import datetime, timezone
from pickle import STOP

from django.db import models
from django.utils import timezone as django_timezone


# Create your models here.
class Timer(models.Model):
    STOPPED = 0
    RUNNING = 1
    TIMER_STATUS = [(STOPPED, "Stopped"), (RUNNING, "Running")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    timer_count = models.SmallIntegerField(default=0, null=False)
    status = models.SmallIntegerField(choices=TIMER_STATUS, default=0, null=False)

    def __str__(self) -> str:
        return str(self.title)

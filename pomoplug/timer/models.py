import uuid

from config.settings import DEFAULT_TIMER_VALUE
from django.db import models


# Create your models here.
class Timer(models.Model):
    STOPPED = 0
    RUNNING = 1
    TIMER_STATUS = [(STOPPED, "Stopped"), (RUNNING, "Running")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    timer_count = models.SmallIntegerField(default=0, null=False)
    current_value = models.SmallIntegerField(default=DEFAULT_TIMER_VALUE, null=False)
    status = models.SmallIntegerField(choices=TIMER_STATUS, default=0, null=False)
    user = models.ForeignKey(
        "auth.User",
        related_name="timers",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)

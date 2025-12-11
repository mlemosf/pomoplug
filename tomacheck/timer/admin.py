from django.contrib import admin

from .models import Timer


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "timer_count", "status")
    list_filter = ("status",)
    search_fields = ("title",)

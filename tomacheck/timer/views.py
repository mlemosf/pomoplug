from django.shortcuts import render
from django.views.generic import TemplateView

from timer.models import Timer


# Create your views here.
class TimerView(TemplateView):
    template_name = "timer.html"

    def get_context_data(self, **kwargs):
        timer_uuid = kwargs.get("uuid")
        print(timer_uuid)
        timer = Timer.objects.get(id=timer_uuid)
        context = super().get_context_data(**kwargs)
        context["title"] = timer.title
        return context

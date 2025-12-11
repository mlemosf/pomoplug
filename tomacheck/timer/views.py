from http.client import NOT_FOUND

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView, TemplateView

from timer.models import Timer


# Create your views here.
class TimerCreateView(RedirectView):
    permanent = False
    query_string = False
    pattern_name = "timer-view"

    def get_redirect_url(self, *args, **kwargs):
        title = self.request.GET.get("t", None)
        try:
            timer = Timer.objects.get(title=title)
        except ObjectDoesNotExist:
            timer = Timer.objects.create(title=title)
        finally:
            kwargs["uuid"] = timer.id
            return super().get_redirect_url(*args, **kwargs)


class TimerView(TemplateView):
    template_name = "timer.html"

    def get_context_data(self, **kwargs):
        timer_uuid = kwargs.get("uuid")
        print(timer_uuid)
        timer = Timer.objects.get(id=timer_uuid)
        context = super().get_context_data(**kwargs)
        context["title"] = timer.title
        context["count"] = timer.timer_count
        return context

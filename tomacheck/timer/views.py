import json
from http.client import NOT_FOUND

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView, TemplateView, View

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
            kwargs["uuid"] = timer.id
            return super().get_redirect_url(*args, **kwargs)
        except ObjectDoesNotExist:
            timer = Timer.objects.create(title=title)
            kwargs["uuid"] = timer.id
            return super().get_redirect_url(*args, **kwargs)


class TimerView(View):
    def get(self, request, *args, **kwargs):
        timer_uuid = kwargs.get("uuid")
        timer = Timer.objects.get(id=timer_uuid)
        context = {
            "uuid": timer.id,
            "title": timer.title,
            "current_value": timer.current_value,
            "count": timer.timer_count,
        }
        return render(request, template_name="timer.html", context=context)

    def put(self, request, *args, **kwargs):
        timer_id = kwargs.get("uuid", None)
        body = json.loads(request.body)

        # TODO: Add proper body validation
        timer = Timer.objects.get(id=timer_id)
        timer.status = body.get("status", timer.status)
        timer.current_value = body.get("current_value", timer.current_value)
        timer.timer_count = body.get("timer_count", timer.timer_count)
        timer.save()

        timer_dict = {
            "title": timer.title,
            "current_value": timer.current_value,
            "count": timer.timer_count,
        }

        return JsonResponse(
            timer_dict,
            content_type="application/json",
        )

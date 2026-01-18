import json
from http.client import NOT_FOUND

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView, TemplateView, View
from django.core.exceptions import PermissionDenied

from timer.models import Timer


# Create your views here.
class TimerCreateView(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = False
    pattern_name = "timer-view"
    login_url = "/login"
    redirect_field_name = "redirect_to"

    def get_redirect_url(self, *args, **kwargs):
        title = self.request.GET.get("t", None)
        user = self.request.user
        try:
            timer = Timer.objects.get(title=title)
            kwargs["uuid"] = timer.id
            return super().get_redirect_url(*args, **kwargs)
        except ObjectDoesNotExist:
            user = user
            timer = Timer.objects.create(title=title, user=user)
            kwargs["uuid"] = timer.id
            return super().get_redirect_url(*args, **kwargs)


class TimerView(LoginRequiredMixin, View):
    login_url = "/login"
    redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        try:
            timer_uuid = kwargs.get("uuid")
            user = request.user
            # TODO: Ordenar por data de criacao
            timers = Timer.objects.filter(user=user).order_by("title")
            timer_list = timers.values("id", "title")
            timer = timers.get(id=timer_uuid)
            context = {
                "uuid": timer.id,
                "title": timer.title,
                "current_value": timer.current_value,
                "count": timer.timer_count,
                "status": timer.status,
                "timer_list": timer_list,
            }
            return render(request, template_name="main.html", context=context)
        except ObjectDoesNotExist:
            return render(request, status=404, template_name="404.html")

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

    def delete(self, request, *args, **kwargs):
        timer_id = kwargs.get("uuid", None)
        try:
            timer = Timer.objects.get(id=timer_id)
            timer.delete()
            return JsonResponse({}, content_type="application/json")
        except ObjectDoesNotExist:
            return JsonResponse({}, content_type="application/json")
